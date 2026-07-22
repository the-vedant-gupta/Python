def add_item(x):
    x += 1
    print(f"Inside fn: {x}")


nums = 10
add_item(nums)
print(f"Outside fn: {nums}")
