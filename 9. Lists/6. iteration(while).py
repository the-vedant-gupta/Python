num = [34, 52, 42, 55, 22]

n = len(num)
# i = 0
# count = 0
# while i <= n - 1:
#     if num[i] % 2 == 0:
#         count += 1
#     i += 1
# print(count)

i = n - 1
while i >= 0:
    print(num[i], end=" ")
    i -= 1
