"""
Write a function that ask a number from user and
prints if that number is odd or even
"""

# def number(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# number(10)
# number(23)


def odd_even():
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


odd_even()
odd_even()
