class Animal:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


d1 = Dog("Abc", 3)
d1.sleep()
d1.speak()
d1.bark()
