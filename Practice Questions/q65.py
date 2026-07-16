"""
Given a marks, use list comprehesnion to create a new list that contains
only the marks are above 75.
"""

marks = [45, 33, 77, 86, 45, 97, 87, 85]

new_lst = [i for i in marks if i >= 75]
print(new_lst)
