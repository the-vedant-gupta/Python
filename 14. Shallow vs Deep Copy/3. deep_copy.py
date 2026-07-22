import copy

original = [1, 2, 3, [34, 65, 4], 5, 7]
# shallow = original.copy()
shallow = copy.deepcopy(original)

print(id(original))
print(id(shallow))

shallow[3][2] = 23

print(original)
print(shallow)
