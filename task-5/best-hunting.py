import random as rnd
import numpy as np
import math
import matplotlib.pyplot as plt
rnd.seed(42)
area = (5000, 5000)
home = (area[0] / 2, area[1] / 2)
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
class Cat:
    def __init__(self, name, preferences, zone):
        self.name = name
        self.preferences = preferences
        self.available_time = 7200  # 2 hours in sec
        self.collected_objects = []  # 10cm->1s
        self.position = home
        self.path = []
        self.score = 0
        self.zone = zone
    def find_best_item(self, hunt_items):
        best_item = None
        best_value = -1
        for item in hunt_items:
            if item.name in self.preferences and self.preferences[item.name] > 0:
                distance = euclidean_distance(self.position, item.position)
                total_time = distance / 10.0 + item.time
                value = self.preferences[item.name] / total_time
                if value > best_value:
                    best_value = value
                    best_item = item
        return best_item
    def hunt(self, hunt_items):
        while self.available_time > 0:
            zone_hunt_items = [item for item in hunt_items if item.zone == self.zone]
            if not zone_hunt_items or len(self.collected_objects) == 5:
                self.return_home()
                continue
            best_item = self.find_best_item(zone_hunt_items)
            if not best_item:
                break
            travel_time_to_item = euclidean_distance(self.position, best_item.position) / 10.0
            total_time_for_hunt = travel_time_to_item + best_item.time
            travel_time_home = euclidean_distance(best_item.position, home) / 10.0
            if self.available_time >= total_time_for_hunt + travel_time_home:
                self.available_time -= total_time_for_hunt
                self.score += self.preferences.get(best_item.name, 0)
                self.position = best_item.position
                self.path.append(best_item.position)
                hunt_items.remove(best_item)
                self.collected_objects.append(best_item)
            else:
                break
    def return_home(self):
        time_to_travel = euclidean_distance(self.position, home) / 10.0
        if self.available_time >= time_to_travel:
            self.position = home
            self.available_time -= time_to_travel
            self.path.extend([item.position for item in self.collected_objects] + [home])
            self.collected_objects.clear()
        else:
            self.collected_objects.clear()
class HuntingItem:
    def __init__(self, name, quantity, time, position):
        self.name = name
        self.quantity = quantity
        self.time = time
        self.position = position
        self.zone = None
def place_items():
    items = [
        ('field_mouse', 150, 180),
        ('house_mouse', 80, 120),
        ('snail', 90, 90),
        ('leaf', 300, 60),
        ('rock', 200, 30)]
    hunting_items = []
    for name, quantity, time in items:
        for _ in range(quantity):
            while True:
                position = (rnd.randint(0, area[0]), rnd.randint(0, area[1]))
                if position != home:
                    hunting_items.append(HuntingItem(name, 1, time, position))
                    break
    return hunting_items
def split_zones(hunt_items, cats):
    for item in hunt_items:
        x, y = item.position[0] - home[0], item.position[1] - home[1]
        angle = math.atan2(y, x) % (2 * math.pi)
        if 0 <= angle < 2 * math.pi / 3:
            item.zone = 'zone1'
        elif 2 * math.pi / 3 <= angle < 4 * math.pi / 3:
            item.zone = 'zone2'
        else:
            item.zone = 'zone3'
    zone_counts = {'zone1': {'field_mouse': 0, 'house_mouse': 0, 'snail': 0, 'leaf': 0, 'rock': 0},
                   'zone2': {'field_mouse': 0, 'house_mouse': 0, 'snail': 0, 'leaf': 0, 'rock': 0},
                   'zone3': {'field_mouse': 0, 'house_mouse': 0, 'snail': 0, 'leaf': 0, 'rock': 0}}
    for item in hunt_items:
        zone_counts[item.zone][item.name] += 1
    assigned_zones = set()
    for cat in cats:
        if cat.name == "Luna":
            luna_zone = max((z for z in zone_counts if z not in assigned_zones),
                            key=lambda z: zone_counts[z]['field_mouse'] + zone_counts[z]['house_mouse'])
            cat.zone = luna_zone
            assigned_zones.add(luna_zone)
        elif cat.name == "Ariana":
            ariana_zone = max((z for z in zone_counts if z not in assigned_zones),
                              key=lambda z: zone_counts[z]['snail'])
            cat.zone = ariana_zone
            assigned_zones.add(ariana_zone)
        elif cat.name == "Dante":
            dante_zone = max((z for z in zone_counts if z not in assigned_zones),
                             key=lambda z: zone_counts[z]['rock'] + zone_counts[z]['leaf'])
            cat.zone = dante_zone
    print(f'Ocena obszaru Luny: {zone_counts[luna_zone]["field_mouse"] + zone_counts[luna_zone]["house_mouse"]} / 230')
    print(f'Ocena obszaru Ariany: {zone_counts[ariana_zone]["snail"]} / 90')
    print(f'Ocena obszaru Dantego: {zone_counts[dante_zone]["rock"] + zone_counts[dante_zone]["leaf"]} / 500')
def visualize(cats):
    plt.figure(figsize=(10, 10))
    for cat in cats:
        x, y = zip(*cat.path)
        plt.plot(x, y, marker='o', label=cat.name)
    plt.scatter(*home, color='red', marker='x')
    plt.title('Cats paths')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
def main():
    hunt_items = place_items()
    cats = [
        Cat("Ariana", {'field_mouse': 0.125, 'house_mouse': 0.125, 'snail': 0.375, 'leaf': 0.375, 'rock': 0.0}, {}),
        Cat("Luna", {'field_mouse': 0.4, 'house_mouse': 0.4, 'snail': 0.1, 'leaf': 0.0, 'rock': 0.1}, {}),
        Cat("Dante", {'field_mouse': 0.2, 'house_mouse': 0.2, 'snail': 0.05, 'leaf': 0.05, 'rock': 0.5}, {})
    ]
    split_zones(hunt_items, cats)
    for cat in cats:
        cat.hunt(hunt_items)
    visualize(cats)
if __name__ == '__main__':
   main()
