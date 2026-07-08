"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""


def find_max(a, b, c):
    if a > b and a > c:
        print(f"{a} is max")
    elif b > a and b > c:
        print(f"{b} is max")
    else:
        print(f"{c} is max")


find_max(3, 5, 6)
