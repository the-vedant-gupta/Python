"""
Take a name as input from the user. Print its first character, its last
character, and the total length of the name.
"""

# print(name[0])
# print(name[-1])
# print(len(name))


def print_details(name):
    first = name[0]
    last = name[-1]
    n = len(name)
    print(f"First = {first}, last = {last} and length = {n}")


print_details("vedant")
