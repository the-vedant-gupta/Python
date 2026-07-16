"""
Given a list, remove all duplicate elements while preserving the original
order of the unique itemns
"""

nums = [2, 5, 5, 3, 7, 7, 3, 2, 7, 9, 10, 10]


def remove_duplicate(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result


ans = remove_duplicate(nums)
print(ans)
