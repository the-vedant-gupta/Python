nums = [2, 6, 1, 7, 2, 4, 2, 6, 1, 6, 9, 8]

# print(100 in nums)
# print(1 in nums)

target = int(input("Enter target = "))

if target in nums:
    nums.remove(target)
    print(f"nums = {nums}")
else:
    print("Cannot remove target, target does not exists")
