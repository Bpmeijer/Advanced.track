from Advanced_track.Week_1.advanced_track_section_11_1_1 import Point
from Advanced_track.Week_1.Section_11_2_class import Rectangle

r = Rectangle(Point(100,50), 10, 5)
r.area()
r.perimeter()
r.width == 10 and r.height == 5
r.flip()
r.width == 5 and r.height== 10
print(r.area())
print(r.perimeter())
print(r.width, r.height)