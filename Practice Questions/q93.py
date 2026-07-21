"""
Read a sentence from the user. Count and print the total number of
vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop
"""

text = input("Enter text: ")

total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total += 1
print(f"Total vowel present in text is {total}")
