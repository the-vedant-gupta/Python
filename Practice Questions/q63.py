"""
Write a Python Script that iterate through a list of integers and replaced everey
negative number found in the lsit with the value 0.
"""


def replace_negative(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


nums = [1, 5, -2, -5, -2, 4, 6, -1]
print(replace_negative(nums))
