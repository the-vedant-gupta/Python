marks = [21, 22, 45, 65, 78, 45]

# To get the length
n = len(marks)
print(f"Length of Lists = {n}")

# Max and Mini
maxi = max(marks)
print(f"Maximum marks = {maxi}")
mini = min(marks)
print(f"Minimum marks = {mini}")

# Sum
total = sum(marks)
print(f"Total marks = {total}")

# To spot using sorted(), it will always return you a new list
new_list = sorted(marks, reverse=True)
print(f"New List = {new_list}")
