import copy


def add_item(x):
    x = copy.deepcopy(x)
    x.append(34)
    print(f"Inside fn: {x}")


nums = [2, 5, 6]
add_item(nums)
print(f"Outside fn: {nums}")
