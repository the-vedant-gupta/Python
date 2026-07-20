student = {
    "name": "Vedant",
    "age": 22,
    "gender": "male",
    "city": "Greater Noida",
}
print(student, id(student))

# student.pop("gender")
# student.clear()
del student["age"]
print(student, id(student))
