def rebind(x):
    x = [100, 33, 44]
    print(f"inside fn: {x}")


nums = [1, 2, 3]
rebind(nums)
print(f"Outside function: {nums}")
