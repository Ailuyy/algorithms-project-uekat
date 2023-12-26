from cat_class import Cat
from hunting_item_class import HuntingItem
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
