import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = 1, 2
x2, y2 = 3, 4

distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance is: {distance:.2f}")

