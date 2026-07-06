"""
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(((i - 1) * 5 + j) % 2, end="\t")
#     print()

for i in range(1, 6):
    for j in range(1, 6):
        print((i + j + 1) % 2, end=" ")
    print()
