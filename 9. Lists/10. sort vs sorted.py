nums = [2, 6, 1, 7, 2, 4, 2, 6, 1, 6, 9, 8]

# SORT vs SORTED
# new_list = sorted(nums)
# print(f"new list = {new_list}", id(new_list))
# print(f"nums = {nums}", id(nums))


print(f"nums = {nums}", id(nums))
nums.sort()  # In place sorting
print(f"nums = {nums}", id(nums))
