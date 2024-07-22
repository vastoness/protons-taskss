import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def compute_perimeter():
    points = []
    while True:
        x = input("Enter the x coordinate (or space to finish): ")
        if x == "":
            break
        y = input("Enter the y coordinate: ")
        points.append((float(x), float(y)))
    if len(points) < 3:
        print("A polygon must have at least 3 points.")
        return
    perimeter = 0.0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        perimeter += distance(x1, y1, x2, y2)
    print(f"The perimeter of the polygon is {perimeter:.2f}")
compute_perimeter()
