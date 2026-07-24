class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def bark(self):
        print("Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow!")


class Cow(Animal):
    def moo(self):
        print("Moooo!")


d = Dog("Bruno")
c = Cat("Whisky")
cw = Cow("Bessie")

d.breathe()
c.breathe()
cw.breathe()

d.bark()
c.meow()
cw.moo()
