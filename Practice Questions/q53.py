"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get the count of elements, but avoid using
sum() for total
"""


def calculate_average(lst):
    total = 0
    n = len(lst)
    for num in lst:
        total += num
    return total / n


nums = [23, 53, 62, 13, 62]
print(calculate_average(nums))

ans = calculate_average(nums)
print(f"Average is: {ans:.2f}")
