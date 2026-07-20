marks = {"maths": 94, "english": 33, "hindi": 93}

ans = dict(sorted(marks.items(), key=lambda x: x[0]))
print(ans)
