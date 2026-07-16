"""
Reverse a list without using the .reverse() method or list slicing([::-1]).
"""

nums = [2, 6, 1, 7, 2, 4, 2, 6, 1, 6, 9, 8]

# n = len(nums)
# for i in range(n - 1, 0, -1):
#     print(nums[i], end=" ")
#     i -= 1


def reverse_list(lst):
    n = len(lst)
    new_lst = []
    for i in range(n - 1, 0, -1):
        new_lst.append(lst[i])
    return new_lst


ans = reverse_list(nums)
print(ans)
