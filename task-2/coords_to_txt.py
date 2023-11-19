def to_file(points, txt_file):
   with open("txt_file.txt", "w") as f:
       f.write(f"\n".join(f"{lat} % {lon}" for lat, lon in points) + "\n")
def from_file(txt_file):
   points = []
   with open(txt_file, "r") as f:
       lines = f.readlines()
       for i in range(0, len(lines)):
           x, y = float(lines[i].split('%')[0].split()[0]), float(lines[i].split('%')[1])
           points.append((x, y))
   return points