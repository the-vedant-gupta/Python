"""
Q8: Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""

num1 = int(input("Enter the num1 = "))
num2 = int(input("Enter the num2 = "))

if num1 > num2:
    print(f"{num1} is bigger then num2")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are both equals")
