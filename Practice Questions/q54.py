"""
Given two lists of the same length, wrtie Python code using a loop to create
a new list where each element is the sum of the corresponding elements from
both original lsits.
"""


def sum(lst1, lst2):
    new_lst = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_lst.append(total)
    return new_lst


num1 = [3, -5, 2, 51, -3, 52, 1, 3]
num2 = [76, -2, 34, 51, -34, 2, 54, 11]

print(sum(num1, num2))
