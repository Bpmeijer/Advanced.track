from Advanced_track.Week_1.advanced_track_section_11_1_1 import Point
import math

p = Point(10, 4)
q = Point(4,8)

print(p.x, -p.y, q.x, -q.y)
print(p.distance_from_origin())
print(q.distance_from_origin())
print(p)

print(p.slope_from_origin())
print(q.slope_from_origin())
# when y or x is 0, slope method fails

print("", p.midpoint(q))

def slope(q):
    return ((q.y - p.y) / (q.x - p.x))

def constant(q):
    return (p.y-(slope(q)*p.x))

print(("The slope is "), slope(q))
print(("The constant is"), constant(q))