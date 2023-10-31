import random as rnd, numpy as np, matplotlib.pyplot as plt
rnd.seed(42)
n_points, num_paths, coords_limits = rnd.randint(8, 10), rnd.randint(3, 10), {"min":0.00, "max":50.00}
points = [(round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2), round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2)) for _ in range(n_points)]
paths = [rnd.sample(points, rnd.randint(2, n_points)) for _ in range(num_paths)]
start_point = rnd.choice(points)
end_point = rnd.choice([point for point in points if point != start_point])
k = rnd.randint(1, min(n_points-2, len(points) - 2))
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def find_closest_point(target, points):
    return min(points, key=lambda point: euclidean_distance(target, point))
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
path, total_distance = greedy_algorithm(points, start_point, end_point, k)
# x, y = zip(*points)
# plt.scatter(x, y, color='blue', label='Points', s=100)
# x, y = zip(*path)
# plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5, label='Path')
# plt.scatter(*start_point, color='orange', label='Start Point', s=100)
# plt.scatter(*end_point, color='red', label='End Point', s=100)
# plt.legend()
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.title('Shortest Path')
# plt.show()
with open("txt_file.txt", "w") as f:
    f.write(f"Number of points: {n_points}\nNumber of paths: {num_paths}\n\n")
    f.write("Points:\n" + "\n".join(f"Point: x = {lat} y = {lon}" for lat, lon in points) + "\n\n")
    f.write("Paths:\n" + "\n".join(f"Path: {';'.join(f'x = {lat} y = {lon}' for lat, lon in path_points)}" for path_points in paths) + "\n\n")
    f.write(f"Start point: {start_point}\nEnd point: {end_point}\n")
    f.write(f"Shortest Path: {';'.join(f'x = {lat} y = {lon}' for lat, lon in path)}\nTotal Distance: {total_distance}")