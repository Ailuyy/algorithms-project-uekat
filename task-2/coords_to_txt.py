def to_file(n_points, points, txt_file):
    with open("txt_file.txt", "w") as f:
        f.write(f"Number of points: {n_points}\n\nPoints:\n" + "\n".join(f"Point: x = {lat} y = {lon}" for lat, lon in points) + "\n\n")
def from_file(txt_file):
    points = []
    with open(txt_file, "r") as f:
        lines = f.readlines()
        n_points = len(lines)
        num_paths = int(lines[1].split(":")[-1].strip())
        for i in range(2, 2 + n_points):
            x, y = float(lines[i].split("x =")[-1].split()[0]), float(lines[i].split("y =")[-1])
            points.append((x, y))
    return n_points, points