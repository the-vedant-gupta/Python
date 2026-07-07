"""
Write a function that prints all the factors of a
number entered by user
"""


def print_factor():
    num = int(input("Enter the number: "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


print_factor()
