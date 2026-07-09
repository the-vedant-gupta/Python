"""
Create a list of 5 numbers. Print the first, last and middle number
from your list using both positive and negative indexing where appropriate

"""

lst = [34, 64, 52, 63, 23, 23, 35, 14]

n = len(lst)
print(f"First Element: {lst[0]}")
print(f"Last Element: {lst[-1]}")
print(f"Middle Element: {lst[n//2]}")
