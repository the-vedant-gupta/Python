class Money:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __eq__(self, other) -> bool:
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __gt__(self, other):
        return self.amount > other.amount


a = Money(33)
b = Money(33)
print(a == b)

a = Money(33)
b = Money(11)
print(a < b)
