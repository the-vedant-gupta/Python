"""
Given two lists, merge into a single new list
withot modifying the original
"""

# def merge_list(lst1, lst2):
#     return lst1 + lst2


def merge_list(lst1, lst2):
    new_lst = []
    for i in lst1:
        new_lst.append(i)
    for i in lst1:
        new_lst.append(i)
    return new_lst


num1 = [2, 36, 64]
num2 = [2, 3, 6]

print(merge_list(num1, num2))
