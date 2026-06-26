# start and end by user
# start to end print using while loop

start = int(input("Enter the starting num: "))
end = int(input("Enter the ending num: "))
i = start

while i <= end:
    print(i, end=" ")
    i += 1

print(f"\nAfter while loop, start value is {start}")
