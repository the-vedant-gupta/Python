"""
Subjects and Marks
Create a dictionary of 6 subjects and their rspective marks.
Print the subjects with the highest marks and the one with the lowest,
using max() and min() functions alongside a lambda expression
"""

subjects = {
    "Mathematics": 88,
    "Science": 95,
    "English": 72,
    "History": 80,
    "Geography": 67,
    "Computer": 91,
}

maxi = max(subjects.items(), key=lambda x: x[1])
print(maxi)

mini = min(subjects.items(), key=lambda x: x[1])
print(mini)
