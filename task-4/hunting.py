import random as rnd
import math
import numpy as np
import matplotlib.pyplot as plt
rnd.seed(42)
class Cat:
    def __init__(self, name, preferences):
       self.name = name
       self.preferences = preferences
       self.available_time = 7200  # 2 hours in sec
       self.zone = []
       self.collected_objects = []  # 10cm->1s
       self.position = home
       self.path = []
       self.score = 0
class HuntingItem:
    def __init__(self, name, quantity, time):
        self.name = name
        self.quantity = quantity
        self.time = time

area_width, area_height, home_x, home_y = 5000, 5000, 2500, 2500
area = (area_width, area_height)
home = (area_width / 2, area_height / 2)


def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# def split_zones(hunt_items, cats):

def main():
    rnd.seed(42)
    hunt_objects = [HuntingItem('field_mouse', 150, 180), HuntingItem('house_mouse', 80, 120),
                    HuntingItem('snail', 90, 90),
                    HuntingItem('leaf', 300, 60), HuntingItem('rock', 200, 30)]
    cats = [Cat("Ariana", {'field_mouse': 0.125, 'house_mouse': 0.125, 'snail': 0.375, 'leaf': 0.375, 'rock': 0.0}),
            Cat("Luna", {'field_mouse': 0.4, 'house_mouse': 0.4, 'snail': 0.1, 'leaf': 0.0, 'rock': 0.1}),
            Cat("Dante", {'field_mouse': 0.2, 'house_mouse': 0.2, 'snail': 0.05, 'leaf': 0.05, 'rock': 0.5})]
    all_preys = []

    for item in hunt_objects:
        placed_items = set()
        for _ in range(item.quantity):
            while True:
                x, y = rnd.randint(0, area_width - 1), rnd.randint(0, area_height - 1)
                if (x, y) not in area and x != home_x and y != home_y:
                    all_preys.append(((x, y), item.name, item.time))
                    placed_items.add((x, y))
                    break
