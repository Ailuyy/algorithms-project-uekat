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