"""
Reverse Word Order
Take a sentence as input. Reverse the order of words (not the
characters in each word). Example: "Python is fun" → "fun is Python".
"""


def reverse_word(sentence: str):
    word = sentence.split()
    word = word[::-1]
    return " ".join(word)


sentence = "Vedant is a Python Developer"
print(reverse_word(sentence))
