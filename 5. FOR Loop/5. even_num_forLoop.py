# Even Numbers using for Loop

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

total = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
        total += 1

print(f"\nTotal even no is {total}")
