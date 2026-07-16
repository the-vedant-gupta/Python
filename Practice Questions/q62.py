"""
Given a list of numbers, write a python script
that takes an integer as input from the user and removes all occurrences of that integer from the list.
"""

# def remove_occurence(lst, target):
#     new_lst = []
#     for num in lst:
#         if num != target:
#             new_lst.append(num)
#     return new_lst


def remove_occurence(lst, target):
    while target in lst:
        lst.remove(target)
    return lst


nums = [1, 1, 3, 5, 2, 5, 3, 2, 5, 6, 3]
print(remove_occurence(nums, 1))
