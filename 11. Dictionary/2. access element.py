marks = {
    "science": 95,
    "maths": 33,
    "hindi": 34,
    "comp": 55,
}

# print(marks["hindi"])
# print(marks.get("comp"))
# print(marks.get("compp", 0))

subject = "comp"

ans = marks.get(subject)
if ans is None:
    print("Subject not Found")
else:
    print(f"Marks get: {ans}")

