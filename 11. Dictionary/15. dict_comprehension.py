square = {i: i * i for i in range(1, 6)}
print(square)


marks = {"maths": 54, "english": 95, "comp": 87}

top = {sub: m for sub, m in marks.items() if m >= 75}
print(top)


double = {sub: 2 * m for sub, m in marks.items()}
print(double)

subjects = ["maths", "comp", "english"]
mark = [84, 45, 64]

result = {sb: m for sb, m in zip(subjects, mark)}
print(result)
