"""
Write a function fizzbuzz(n) that takes a single number and prints "Fizz"
if it divisible by 3, "Buzz" if it is divisible by 5, "FizzBuzz"
if it's divisible by both, otherwise print the number itself
"""


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n


num = fizzbuzz(7)
print(num)
