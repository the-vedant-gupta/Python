"""
Create a tuple of marks of 6 students. Print the highest, lowest, total and average.
"""

marks = (45, 65, 87, 45, 33, 55)

n = len(marks)

print(f"Highest is : {max(marks)}")
print(f"Lowest is : {min(marks)}")
total = sum(marks)
print(f"Total is: {total}")
print(f"Average is : {total // n}")


# def marks_insights(tpl):
#     n = len(marks)
#     maxi = float("-inf")
#     min = marks[0]
#     total = 0
#     for i in tpl:
#         if i > maxi:
#             maxi = i
#         if i < min:
#             min = i
#         total += i
#         average = total / n
#     return maxi, min, total, average


# print(marks_insights(marks))
