import random as rnd
n_points, num_paths, coords_limits = rnd.randint(2, 10), rnd.randint(1, 5), {"min":0.00, "max":50.00}
points = [(round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2), round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2)) for _ in range(n_points)]
paths = [rnd.sample(points, rnd.randint(2, n_points)) for _ in range(num_paths)]
with open("txt_file.txt", "w") as f:
    f.write(f"Number of points: {n_points}\nNumber of paths: {num_paths}\n")
    f.writelines([f"Point: x = {lat:.2f} y = {lon:.2f}\n" for lat, lon in points])
    f.writelines([f"Path: {';'.join([f'x = {lat:.2f} y = {lon:.2f}' for lat, lon in path_points])}\n" for path_points in paths])