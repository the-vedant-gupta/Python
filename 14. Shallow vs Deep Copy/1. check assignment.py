original = [1, 2, 3]
copy = original

copy.append(33)
print(id(original))
print(id(copy))

print(original is copy)
print(original == copy)

print(copy)
print(original)
