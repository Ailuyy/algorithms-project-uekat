import random as rnd
def random_data():
    n_points, num_paths, coords_limits = rnd.randint(2, 10), rnd.randint(1, 5), {"min":0.00, "max":50.00}
    points = [(round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2), round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2)) for _ in range(n_points)]
    paths = [rnd.sample(points, rnd.randint(2, n_points)) for _ in range(num_paths)]
    return n_points, num_paths, points, paths
def to_file(txt_file):
    data = random_data()
    with open(txt_file, "w") as f:
        f.write(f"Number of points: {data.n_points}\nNumber of paths: {data.num_paths}\n")
        f.writelines([f"Point: x = {lat:.2f} y = {lon:.2f}\n" for lat, lon in data.points])
        f.writelines([f"Path: {';'.join([f'x = {lat:.2f} y = {lon:.2f}' for lat, lon in path_points])}\n" for path_points in data.paths])
def from_file(txt_file):
    points, paths = [], []
    with open(txt_file, "r") as f:
        lines = f.readlines()
        n_points = int(lines[0].split(":")[-1].strip())
        num_paths = int(lines[1].split(":")[-1].strip())
        for i in range(2, 2 + n_points):
            x, y = float(lines[i].split("x =")[-1].split()[0]), float(lines[i].split("y =")[-1])
            points.append((x, y))
        for i in range(2 + n_points, len(lines)):
            path = [(float(pair.split('x =')[1].split()[0]), float(pair.split('y =')[1])) for pair in lines[i].split(':')[1].strip().split(';')]
            paths.append(path)
    return n_points, num_paths, points, paths