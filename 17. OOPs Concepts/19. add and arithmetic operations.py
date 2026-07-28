class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __add__(self, other):
        return self.km + other.km

    def __sub__(self, other):
        return self.km - other.km

    def __mul__(self, times):
        return self.km * times

    def __str__(self, other):
        return f"{self.km} km"


d1 = Distance(33)
d2 = Distance(3)

print(d1.km + d2.km)
print(d1.km - d2.km)
print(d1 * 3)
print(d1.km)
