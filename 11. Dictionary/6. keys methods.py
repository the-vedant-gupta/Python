marks = {
    "science": 75,
    "maths": 87,
    "hindi": 96,
    "comp": 99,
    "history": 65,
}

# print(marks.keys())

total = 0
for sub in marks.keys():
    # print(sub, marks[sub])
    print(f"Subject: {sub} and marks: {marks[sub]}")
    total += marks[sub]

print(total)
