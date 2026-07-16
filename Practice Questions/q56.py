"""
Find the largest and smallest num in a list without
using built-in functios like max() and min()
"""

nums = [2, 6, 2, 7, 3, 5, 1]

n = len(nums)

max = float("-inf")
min = nums[0]

for i in nums:
    if i > max:
        max = i
print(f"Max number is : {max}")

# for j in nums:
if i < min:
    min = i
print(f"Min number is : {min} ")
