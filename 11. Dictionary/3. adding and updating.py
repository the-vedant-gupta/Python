student = {
    "name": "Vedant",
    "age": 22,
}

print(student, id(student))

# Update
student["age"] = 21

# Add
student["Gender"] = "Male"

student.update(
    {
        "city": "Greater Noida",
        "phone": 9394455,
    }
)

print(student, id(student))
