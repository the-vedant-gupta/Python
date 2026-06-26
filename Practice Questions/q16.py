"""
Sum of all the numbers from 1 to 100.
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
i = start
sum = 0

while i <= end:
    sum += i
    i += 1

print(f"Total = {sum}")
