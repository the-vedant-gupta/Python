"""
Student Details
Create a nested dictionary containing details for 4 students, where each student
entry includes their name, age and city. Write a loop to print the full details
of each student in a clear readable format
"""

students = {
    1: {"name": "Aarav", "age": 18, "city": "Delhi"},
    2: {"name": "Priya", "age": 19, "city": "Mumbai"},
    3: {"name": "Rahul", "age": 20, "city": "Bengaluru"},
    4: {"name": "Sneha", "age": 18, "city": "Hyderabad"},
}

for k, v in students.items():
    print(
        f" Roll No. : {k} and Details : Name = {v["name"]}, age = {v["age"]}, city = {v["city"]} "
    )
