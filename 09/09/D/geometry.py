# Fill your boots here...

import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def delta_x(self, dx):
        return Point(self.x + dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y + dy)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)


class Rectangle:

    def __init__(self, upper_left: Point, lower_right: Point):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __repr__(self):
        return f"Rectangle(Point({self.upper_left.x}, {self.upper_left.y}), Point({self.lower_right.x}, {self.lower_right.y}))"

    def __str__(self) -> str:
        return f"Rectangle(Point({self.upper_left.x}, {self.upper_left.y}), Point({self.lower_right.x}, {self.lower_right.y}))"

    def translate(self, dx, dy):
        return Rectangle(Point(self.upper_left.x + dx, self.upper_left.y + dy),Point(self.lower_right.x + dx, self.lower_right.y + dy))

    def perimeter(self):
        return abs((self.lower_right.x - self.upper_left.x)) * 2 + abs((self.upper_left.y - self.lower_right.y)) * 2

    def area(self):
        return abs((self.lower_right.x - self.upper_left.x) * (self.upper_left.y - self.lower_right.y))


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(Point({self.center.x}, {self.center.y}), {self.radius})"

    def __str__(self) -> str:
        return f"Circle(Point({self.center.x}, {self.center.y}), {self.radius})"

    def translate(self, dx, dy):
        return Circle(Point(self.center.x + dx, self.center.y + dy), self.radius)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


