import random as rnd, numpy as np, coords_to_txt as coords
rnd.seed(42)
def generate_points(k):
   n_points, coords_limits = rnd.randint(k, k + rnd.randint(10, 100)), {"min":0.00, "max":50.00}
   points = [(round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2), round(rnd.uniform(coords_limits["min"], coords_limits["max"]), 2)) for _ in range(n_points)]
   return points
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
def main():
   k = int(input("How many K points do you need?\n"))
   decision = input("Do you want to import points from data.txt? Y/N\n")
   points = coords.from_file("data.txt") if str.upper(decision) == "Y" else generate_points(k)
   start_point = rnd.choice(points)
   end_point = rnd.choice([point for point in points if point != start_point])
   path, total_distance = greedy_algorithm(points, start_point, end_point, k)
   coords.to_file(points, "txt_file.txt") if str.upper(decision) == "N" else ""
   print(f"Start point: {start_point}\nEnd point: {end_point}\nN points: {len(points)}\nK points: {k}\nShortest Path: {';'.join(f'x = {lat} y = {lon}' for lat, lon in path)}\nTotal Distance: {round(total_distance, 2)}")
if __name__ == "__main__":
   main()
