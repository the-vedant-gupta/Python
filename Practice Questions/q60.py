"""
Seperate a list of integers into distinct lists: one containing all the
even numbers and other containg all the odd numbers
"""

nums = [2, 6, 2, 7, 3, 5, 1]


def even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(f"Even list = {even}")
    print(f"Odd list = {odd}")


even_odd(nums)
