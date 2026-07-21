text = "Programming"

# in \ not in

# print("P" in text)
# print("z" in text)
# print("z" not in text)
# print("gram" in text)

total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total += 1
print(total)
