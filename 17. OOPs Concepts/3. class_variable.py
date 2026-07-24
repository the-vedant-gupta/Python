class Student:
    school = "M.S. Senior Secondary Public School"

    def __init__(self, name: str) -> None:
        self.name = name


s1 = Student("Vedant")
s2 = Student("Vasu")
print(s1.name)  # instance variable
print(s2.name)  # instance variable

print(s1.school)  # class variable
print(s2.school)  # class variable
print(Student.school)

# Way to change class variable
Student.school = "XYZ"
# s1.school = "ABC"

print(s1.school)  # class variable
print(s2.school)  # class variable
print(Student.school)
