"""
Create a class Circle with attribute radius.
Add methods area() and circumference() that calculate and
return the values. (Use math.pi.)
"""

import math


class Circle:

    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def circumfrence(self) -> float:
        return 2 * math.pi * self.radius

    def get_values(self) -> None:
        print(f"Radius : {self.radius}")
        print(f"Area : {self.area():.2f}")
        print(f"Circumfrence : {self.circumfrence():.2f}")


c1 = Circle(2)
c1.get_values()
