"""
Filter Passing Marks
Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that includes
only the subjects where the student scored 40 or more (i.e., passed).
"""

subjects = {
    "Mathematics": 88,
    "Science": 38,
    "English": 72,
    "History": 23,
    "Geography": 67,
    "Computer": 91,
}

new_dict = {sub: marks for sub, marks in subjects.items() if marks >= 40}
print(new_dict)
