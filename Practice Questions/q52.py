"""
Write a program taht takes a list and a targer number. Use a loop to determine if
the target number exists in the list. Do not use the in operator.
"""


def does_target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False


nums = [23, -53, -62, 13, 62]

print(does_target_exists(nums, 3))
print(does_target_exists(nums, 13))
