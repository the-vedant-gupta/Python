marks = {
    "science": 75,
    "maths": 87,
    "hindi": 96,
    "comp": 99,
    "history": 65,
}

# len() - number of key-values pairs
print(len(marks))

# sum() on values
print(sum(marks.values()))

# min() and max() on values
print(min(marks.values()))
print(max(marks.values()))

# min() and max() on keys (by default it uses keys in sorted alaphabet)
print(min(marks.keys()))
print(max(marks.keys()))


# sorted() on keys - returns a sorted list of keys
print(sorted(marks))

# Sorted dictionary by keys
sorted_by_keys = dict(sorted(marks.items()))
print(sorted_by_keys)
