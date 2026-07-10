"""
Write a program that takes a list of numbers and using a loop, determines
whether it is sorted in ascending order. True if it is sorted,
and False otherwise.
"""

nums = [3, 6, 9, 14, 17, 22, 48, 72, 100]


def is_sorted(lst):
    n = len(lst)
    for i in range(0, n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


print(is_sorted(nums))
