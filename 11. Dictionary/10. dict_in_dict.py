students = {
    "101": {"name": "Vedant Gupta", "age": 21, "city": "Greater Noida"},
    "102": {"name": "Vasu Gupta", "age": 22, "city": "Noida"},
    "103": {
        "name": "Vedant ",
        "age": 20,
        "city": "Dhanaura",
        "details": {"ph no.": 3435, "gender": "male"},
    },
}

# How to Access
# print(students["101"])
# print(students["101"]["name"])
# print(students["103"]["city"])
# print(students["103"]["details"]["ph no."])

for roll_no, details in students.items():
    print(f"roll no = {roll_no} and name = {details['name']}, age = {details['age']}")
