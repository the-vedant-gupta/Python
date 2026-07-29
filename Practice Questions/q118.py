"""
Create a class Counter with a class variable count that tracks
how many Counter objects have been created. Add a class
method get_count() to return it.
"""


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.get_count())
