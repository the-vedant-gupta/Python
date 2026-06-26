"""
Take two numbers as input. Without using *, calculate and print their product using += in a way
that adds first number to itself the second number of times
"""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
product = 0

for i in range(num2):
    product += num1

print(f"Product is {product}")
