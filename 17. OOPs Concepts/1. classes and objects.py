class Student:
    # Attributes
    # roll_no = 0
    # name = " "
    # gender = ""
    # age = 3

    def __init__(self, rollNo: int, name: str, gender: str, age: int) -> None:
        self.roll_no = rollNo
        self.name = name
        self.gender = gender
        self.age = age

    # def set_details(self, rollNo: int, name: str, gender: str, age: int) -> None:
    #     self.roll_no = rollNo
    #     self.name = name
    #     self.gender = gender
    #     self.age = age

    # def set_details(self):
    #     self.roll_no = int(input("Enter the roll no.:"))
    #     self.name = input("Enter the name: ")
    #     self.gender = input("Enter gender: ")
    #     self.age = int(input("Enter age: "))

    def display_details(self) -> None:
        print(f"Roll No. = {self.roll_no}")
        print(f"Name. = {self.name}")
        print(f"Gender. = {self.gender}")
        print(f"Age = {self.age}")


# Object/Instance
student1 = Student(33, "Vedant", "Male", 33)
student1.display_details()


# student2 = Student()
# student2.set_details()
# student2.display_details()
