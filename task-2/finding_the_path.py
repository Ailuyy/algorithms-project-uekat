import random as rnd, numpy as np, matplotlib.pyplot as plt, coords_to_txt as coords
rnd.seed(42)
# TODO: implement options to select export or import of data
def generate_data():
    n_points, coords_limits = rnd.randint(10, 15), {"min":0.00, "max":50.00}
    points = [(round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2), round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2)) for _ in range(n_points)]
    start_point = rnd.choice(points)
    end_point = rnd.choice([point for point in points if point != start_point])
    k = rnd.randint(1, min(n_points - 2, len(points) - 2))
    return n_points, points, start_point, end_point, k
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def find_closest_point(target, all_points):
    return min(all_points, key=lambda point: euclidean_distance(target, point))
def greedy_algorithm(points, start, end, k):
    k_points = [point for point in points if point not in [start, end]]
    current_point = start
    path = [start]
    for _ in range(k):
        closest_point = find_closest_point(current_point, k_points)
        path.append(closest_point)
        k_points.remove(closest_point)
        current_point = closest_point
    path.append(end)
    total_distance = sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))
    return path, total_distance
data = generate_data()
path, total_distance = greedy_algorithm(data[1], data[2], data[3], data[4])
x, y = zip(*data[1])
plt.scatter(x, y, color='blue', label='Points', s=100)
x, y = zip(*path)
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5, label='Path')
plt.scatter(*data[2], color='orange', label='Start Point', s=100)
plt.scatter(*data[3], color='red', label='End Point', s=100)
plt.legend()
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Shortest Path')
plt.show()
coords.to_file(data[0], data[1], "txt_file.txt")
print(f"Start point: {data[2]}\nEnd point: {data[3]}\nK points: {data[4]}\nShortest Path: {';'.join(f'x = {lat} y = {lon}' for lat, lon in path)}\nTotal Distance: {round(total_distance, 2)}")
