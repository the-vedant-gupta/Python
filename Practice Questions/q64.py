"""
Using list comprehension, create a list of square of all
odd numbers from 1 to 20
"""

lst = [i * i for i in range(1, 20) if i % 2 == 1]
print(lst)
