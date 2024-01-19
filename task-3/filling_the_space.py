import random as rnd
class Cat:
    def __init__(self, name, preferences):
       self.name = name
       self.preferences = preferences
       self.available_space = 2000
       self.rating = 0
       self.collected_objects = []
    def fill_space(self, hunt_objects):
        for _ in range(100):
            temp_rating, temp_objects, temp_space = 0, [], self.available_space
            while temp_space > 0:
                added_item = False
                rnd.shuffle(hunt_objects)
                for item in sorted(hunt_objects, key=lambda x: self.preferences.get(x.name, 0), reverse=True):
                    if temp_space >= item.size[0] * item.size[1] * item.size[2] and self.preferences.get(item.name, 0) > 0:
                        temp_objects.append(item)
                        temp_space -= item.size[0] * item.size[1] * item.size[2]
                        temp_rating += 0.5 + 0.5 * self.preferences.get(item.name, 0)
                        added_item = True
                        break
                if not added_item:
                    break
            if temp_rating > self.rating:
                self.rating = temp_rating
                self.collected_objects = temp_objects
        self.available_space = temp_space
class HuntingItem:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def main():
    hunt_objects = [HuntingItem('field_mouse', (5, 3, 3)), HuntingItem('house_mouse', (7, 2, 2)), HuntingItem('snail', (3, 3, 3)), HuntingItem('leaf', (3, 2, 1)), HuntingItem('rock', (2, 2, 1))]
    cats = [Cat("Ariana", {'field_mouse': 0.125, 'house_mouse': 0.125, 'snail': 0.375, 'leaf': 0.375, 'rock': 0.0}),
        Cat("Luna", {'field_mouse': 0.4, 'house_mouse': 0.4, 'snail': 0.1, 'leaf': 0.0, 'rock': 0.1}),
        Cat("Dante", {'field_mouse': 0.2, 'house_mouse': 0.2, 'snail': 0.05, 'leaf': 0.05, 'rock': 0.5})]
    for cat in cats:
       cat.fill_space(hunt_objects)
       loot = {}
       for item in cat.collected_objects:
           loot[item.name] = loot.get(item.name, 0) + 1
       print(f"{cat.name}: Rating: {round(cat.rating, 2)} Loot: {[f'{count}x {item}' if count > 1 else item for item, count in loot.items()]}, Remaining Space: {cat.available_space}")
if __name__ == '__main__':
   main()
