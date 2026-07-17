# 4x5

matrix = [
    [3, 5, 4, 6, 3],
    [7, 2, 4, 5, 7],
    [4, 5, 9, 3, 6],
    [5, 7, 2, 5, 7],
]

rows = len(matrix)
columns = len(matrix[0])
for i in range(0, rows):
    for j in range(0, columns):
        print(matrix[i][j], end=" ")
    print()
