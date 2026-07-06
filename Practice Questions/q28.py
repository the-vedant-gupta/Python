"""
Q28.
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

n = int(input("Enter the num : "))
for i in range(n, 0, -1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()

for i in range(i + 1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()
