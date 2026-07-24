"""
Create a class Rectangle with width and height.
Add methods area(), perimeter(), and is_square()
(returns True if width == height).
"""


class Rectangle:

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def parimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width

    def display_value(self) -> None:
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.parimeter()}")
        print(f"Is Square: {self.is_square()}")


s1 = Rectangle(2, 4)
s1.display_value()
s2 = Rectangle(4, 4)
s2.display_value()
