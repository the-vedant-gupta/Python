"""
Top Scorers
Populate a dictionary with six students names and their corresponding marks.
Loop through it and print the names of all students who achieved a score above 75
"""

students = {
    "Alice": 55,
    "Bob": 94,
    "James": 65,
    "Diana": 82,
    "Frank": 44,
}

for name, marks in students.items():
    if marks >= 75:
        print(f"Name: {name} and Marks: {marks}")
