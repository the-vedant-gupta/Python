"""
Given a 3x3 matrix, print only teh anti-diagonal elemnets
and replace everything else with an asterisk(*)
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
        if i + j == r - 1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
