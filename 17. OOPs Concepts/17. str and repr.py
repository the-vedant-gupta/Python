class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point(x = {self.x}, y = {self.y})"


p = Point(3, 4)
p1 = Point(4, 6)
print(p)
print(p1)
print(repr(p))
print(repr(p1))
