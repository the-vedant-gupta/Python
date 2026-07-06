"""
Take a numbers as input from user one by one. Skip negative
numbers and keep adding the posotive ones. Stop when the user
enters 0 and prints the total. (use both continue and break)
"""

total = 0
while True:
    num = int(input("Enter a number = "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num

print(total)
