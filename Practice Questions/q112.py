"""
Create a class BankAccount with attributes owner and
balance. Add methods deposit(amount) and
withdraw(amount) that update the balance.
Print balance after each operation.
"""


class BankAccount:

    def __init__(self, owner: str, balance: float) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Depositd {amount}. New Balance is {self.balance}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insuficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance {self.balance}")


account = BankAccount("Vedant", 1000)
account.deposit(333)
account.withdraw(100)
