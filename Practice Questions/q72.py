""" """

matrix = [
    [3, 5, 4, 6],
    [7, 2, 4, 5],
    [4, 5, 9, 8],
    [4, 2, 3, 8],
]

r = len(matrix)
c = len(matrix[0])

for i in range(0, r):
    for j in range(0, c):
        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
