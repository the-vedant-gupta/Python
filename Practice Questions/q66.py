"""
Create a 3x3 matrix and then use nested loops to calculate and
print the sum of all its elements
"""

matrix = [
    [3, 5, 4],
    [7, 2, 4],
    [4, 5, 9],
]

rows = len(matrix)
columns = len(matrix[0])

total = 0
for i in range(0, rows):
    for j in range(0, columns):
        total += matrix[i][j]

print(total)
