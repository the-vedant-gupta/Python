student = {
    "name": "Vedant",
    "age": 22,
    "gender": "male",
    "city": "Greater Noida",
}

k = input("Enter key = ")

if k in student:
    print(student[k])
else:
    print("Key does not exist")
