"""
Create a class Product with instance variables name and price.
Add a class variable tax_rate = 0.18.
Add an instance method final_price() that uses the class variable.
"""


class Product:
    tax_rate = 0.18

    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: int = price

    def final_price(self):
        return self.price * (1 + Product.tax_rate)


p1 = Product("Laptop", 10000)
print(p1.final_price())
