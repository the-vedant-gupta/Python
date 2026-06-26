"""
Print all the numbers which are divisible by 3 and 5, from 1 to 100.
"""

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
i = start

while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1
