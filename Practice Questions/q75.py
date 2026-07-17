"""
Take a 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.
"""

tpl = ()
for i in range(5):
    mark = int(input("Enter the marks: "))
    tpl += (mark,)
print(tpl)
maxi = float("-inf")
mini = float("inf")

for i in tpl:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i


print(mini)
print(maxi)
