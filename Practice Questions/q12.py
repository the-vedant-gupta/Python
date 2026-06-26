"""
Take a three numbers as input. Print the largest of the
three without using any built in function
"""

num1 = int(input("Enter the num1 = "))
num2 = int(input("Enter the num2 = "))
num3 = int(input("Enter the num3 = "))


if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num1} and {num2}")
