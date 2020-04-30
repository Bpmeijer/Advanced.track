from Advanced_track.Week_1.advanced_track_section_11_1_1 import Point


class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, delta_x, delta_y):
        self.corner.x = delta_x
        self.corner.y = delta_y

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, point):
        return (self.corner.x <= point.x < (self.corner.x + self.width)) and \
               (self.corner.y <= point.y < (self.corner.y + self.height))

    def contains_alternative(self, point):
        inside = True

        if self.corner.x > point.x:
            inside = False
        if point.x >= (self.corner.x + self.width):
            inside = False
        if self.corner.y > point.y:
            inside = False
        if point.y >= (self.corner.y + self.height):
            inside = False

        return inside

    def get_corners(self):
        top_left = self.corner
        top_right = Point(self.corner.x + self.width, self.corner.y)
        bottom_left = Point(self.corner.x, self.corner.y + self.height)
        bottom_right = Point(self.corner.x + self.width, self.corner.y + self.height)
        return [top_left, top_right, bottom_left, bottom_right]

    def collide(self, other_rectangle):
        colliding = False
        for corner in self.get_corners():
            if other_rectangle.contains(corner):
                colliding = True
        for corner in other_rectangle.get_corners():
            if self.contains(corner):
                colliding = True
        return colliding

    if __name__ == "__main__":
        # this only gets executed when the file is run directly, not when it is included in another
        box = Rectangle(Point(0, 0), 100, 200)
        bomb = Rectangle(Point(100, 80), 5, 10)

        print("box ", box)
        print("bomb ", bomb)

        box.grow(50, -50)
        print("box ", box)

        box.move(100, 80)
        print("box ", box)


box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)