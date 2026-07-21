"""
Given a string input, print every alternate character starting from the
very first character, using string slicing.
"""

text = input("Enter text: ")

# print(text[::2])


def slicing(text):
    return text[::2]


ans = slicing(text)
print(ans)
