"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num = int(input("Enter the num: "))
i = 1
count = 0

while i <= num:
    if num % i == 0:
        count += 1
        print(i, end=" ")
    i += 1

print(f"\nTotal factors of {num} are {count}  ")
