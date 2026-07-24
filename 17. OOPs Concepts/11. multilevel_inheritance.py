class Animal:
    def breate(self):
        print("Breathing...")


class Mammal(Animal):
    def feed_young(self):
        print("Feed Young....")


class Dog(Mammal):
    def bark(self):
        print("Woof!")


d = Dog()
d.breate()
d.feed_young()
d.bark()
