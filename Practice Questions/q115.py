"""
Create a class Employee with name, salary, and department.
Add a method give_raise(amount) that increases salary.
Create 3 employees and give one of them a raise.

"""


class Employee:

    def __init__(self, name: str, salary: int, department: str) -> None:
        self.name: str = name
        self.salary: int = salary
        self.department: str = department

    def give_raise(self, amount: int) -> None:
        self.salary += amount
        print(f"{self.name} reveived a raise of {amount}.")

    def display(self):
        print(
            f"Name: {self.name}| Department: {self.department} | Salary: {self.salary}"
        )


emp1 = Employee("Aarav", 45000, "Engineering")
emp2 = Employee("Priya", 52000, "Marketing")
emp3 = Employee("Rohan", 38000, "Sales")

print("--- Before Raise ---")
for emp in (emp1, emp2, emp3):
    emp.display()

emp1.give_raise(5000)
emp2.give_raise(5000)
emp3.give_raise(5000)

print("\n--- After Raise ---")
for emp in (emp1, emp2, emp3):
    emp.display()
