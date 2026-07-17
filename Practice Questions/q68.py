"""
Given a 3x3 matrix, print its upper traingle.
Replace all elements in the lower traingle with an asterisk(*)
"""

matrix = [
    [3, 5, 4],
    [7, 2, 4],
    [4, 5, 9],
]

r = len(matrix)
c = len(matrix[0])

for i in range(0, r):
    for j in range(0, c):
        if i <= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
