"""
Take a number as input. Using ternary operator,
print "Even" or "Odd" in a single line
"""

num = int(input("Enter the number= "))

status = "Even" if num % 2 == 0 else "Odd"
print(f"number is {status}")
