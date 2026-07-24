class Animal:
    def speak(self):
        print("Animal is speaking")

    def display(self):
        print("This is a display")


class Dog(Animal):
    def speak(self):
        super().speak()
        self.display()
        print("Dog is barking")


d = Dog()
d.speak()
