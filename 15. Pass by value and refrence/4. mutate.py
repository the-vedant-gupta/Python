def mutate(x):
    x[2] = 11
    x.append(23)
    print(f"inside fn: {x}")


nums = [1, 2, 3]
mutate(nums)
print(f"Outside function: {nums}")
