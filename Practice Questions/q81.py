"""
Subject Performance Analysis
Given a dictionary of marks for different subjects, loop over its values() to calculate and print
the total marks and the average marks obtained
"""


def total_average(lst):
    n = len(lst)
    total = 0
    for marks in lst.values():
        total += marks
    average = total / n
    return total, average


subject_marks = {
    "Hindi": 34,
    "English": 45,
    "Comp": 76,
    "History": 55,
    "Maths": 98,
}
Total, Average = total_average(subject_marks)
print(f"Total : {Total}")
print(f"Average : {Average}")

# n = len(subject_marks)
# total_marks = sum(subject_marks.values())
# print(total_marks)
# average_marks = total_marks / n
# print(average_marks)
