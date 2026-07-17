# Make a function which return min and max of a list


def min_max(lst):
    mini = min(lst)
    maxi = max(lst)
    return mini, maxi


ans1, ans2 = min_max([3, 5, 6, 8, 2, 9, 3])
print(f"maximum number is {ans2}")
print(f"minimum number is {ans1}")
