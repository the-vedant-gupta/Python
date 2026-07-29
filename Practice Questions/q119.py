"""
Create a class Temperature with an instance variable celsius.
Add a class method from_fahrenheit(f) that creates a Temperature
object from a Fahrenheit value.
"""


class Temperature:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5 / 9
        return cls(celsius)


t1 = Temperature(65)
print(t1.celsius)

t2 = Temperature.from_fahrenheit(33)
print(t2.celsius)
