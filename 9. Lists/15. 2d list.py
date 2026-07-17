# 3x3

matrix = [
    [3, 5, 4],
    [7, 2, 4],
    [4, 5, 9],
]

# print(matrix[0])

total = 0
for i in range(0, 3):
    for j in range(0, 3):
        total += matrix[i][j]
        # print(matrix[i][j], end=" ")
    # print()

print(total)
