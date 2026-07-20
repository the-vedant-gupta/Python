marks = {
    "science": 75,
    "maths": 87,
    "hindi": 96,
    "comp": 99,
    "history": 65,
}

# print(marks.values())

total = 0
for mark in marks.values():
    # print(mark)
    total += mark
print(total)
