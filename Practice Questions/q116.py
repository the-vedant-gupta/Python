"""
Create a class Calculator with methods add (a, b), subtract(a, b),
multiply(a, b), divide(a, b). Handle division by zero.
"""


class Calculator:

    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed"
        return self.a / self.b


cacl = Calculator(12, 4)
print(cacl.multiply())
