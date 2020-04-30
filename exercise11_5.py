from Advanced_track.Week_1.advanced_track_section_11_1_1 import Point
import math

p = Point(100,50)
q = Point(200,100)
r = Point(300,150)
s = Point(400,200)

west = min(p.x, q.x, r.x, s.x)
east = max(p.x, q.x, r.x, s.x)
north = max(p.y, q.y, r.y, s.y)
south = min(p.y, q.y, r.y, s.y)

x = (west+east)/2
y = (north+south)/2

print(x,y)