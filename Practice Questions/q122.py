"""
Add a method to Product from Q4 that lets you update the
class-level tax_rate for ALL products at once.
Should it be a class method or static method? Hint: class method.
"""


class Product:
    tax_rate = 0.18

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def final_price(self):
        return self.price * (1 + Product.tax_rate)

    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate


p1 = Product("Laptop", 10000)
print(p1.final_price())

Product.set_tax_rate(0.25)

print(p1.final_price())
