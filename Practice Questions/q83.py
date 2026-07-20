"""
Dictionary Merge Function
Write a Python function named merge_dict(d1,d2) that accepts two dictionaries
(d1 and d2) as argumnets and returns a new dictionary formed by merging them
using the update() method. Ensure d1 remians unchanged
"""


def merge_dict(dict1, dict2):
    new_dict = {}
    new_dict.update(dict1)
    new_dict.update(dict2)
    return new_dict


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"e": 4, "f": 5, "g": 6}

ans = merge_dict(d1, d2)
print(ans)
