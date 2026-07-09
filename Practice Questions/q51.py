"""
Find the Largest Element.
-> without using built-in max() function
"""

numbers = [-23, -53, -62, -13, -62]


maxi = float("-inf")

for num in numbers:
    if num > maxi:
        maxi = num
print(f"Maximum number = {maxi}")
