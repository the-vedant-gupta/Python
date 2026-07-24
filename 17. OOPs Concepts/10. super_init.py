class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        print("This is Vehicle constructor")


class Car(Vehicle):
    def __init__(self, fuel: str, brand: str) -> None:
        super().__init__(brand)
        print("This is car constructor")
        self.fuel = fuel

    def display(self):
        print(f"You have a {self.brand} car with {self.fuel} type")


car = Car("petrol", "Maruti")
car.display()
