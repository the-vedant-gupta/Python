class Vehicle:
    def __init__(self, brand) -> None:
        self.brand = brand

    def start(self):
        print(f"{self.brand} starting up...")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")


c1 = Car("Maruti")
c1.start()
c1.drive()
