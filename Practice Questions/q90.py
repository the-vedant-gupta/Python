"""
Combine Lists into Dictionary
You have two separate lists: one containing subject names and another containing corresponding marks. Create a dictionary from these two
lists using dictionary comprehension, mapping each subject to its mark.
"""

subjects = ["Maths", "Science", "Computer", "AI/ML"]
marks = [57, 84, 74, 97]

new_dict = {sub: mark for sub, mark in zip(subjects, marks)}
print(new_dict)
