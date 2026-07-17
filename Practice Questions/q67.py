"""
Create a 3x3 matrix as input, print its lower traingle. Replace all elements in the upper triangle
with an asterisk(*)
"""

matrix = [
    [3, 5, 4],
    [7, 2, 4],
    [4, 5, 9],
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        if i >= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
