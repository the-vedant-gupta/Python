"""
Word Lengths
Take a sentence as input. Print each word's length next to it. Example:
Python (6) is (2) great (5).
"""


def word_lenght(sentence: str):
    words = sentence.split()
    for word in words:
        print(f"{word} ({len(word)})", end=" ")


sentence = input("Enter a sentence:")
word_lenght(sentence)
