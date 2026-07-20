"""
Safe Subject Access
Define a dictionary with five subjects and their respective marks.
Utilize the get() method to try accessing that is not in dictionary, ensurig it prints "Not Available" as a default
"""

marks = {
    "science": 75,
    "maths": 87,
    "hindi": 96,
    "comp": 99,
    "history": 65,
}

subject = input("Enter subject name: ")
print("Marks:", marks.get(subject, "Not Available"))

# sub = marks.get(subject)
# if sub is None:
#     print("Subject not found")
# else:
#     print(f"Marks get: {sub}")
