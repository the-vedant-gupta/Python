"""
Unique Words Count
Take a paragraph as input. Print the count of unique words in it (case
insensitive)
"""


def unique_word_count(paragraph: str):
    word = paragraph.split()
    return len(set(word))


paragraph = "Vedant is a Pyhton Developer and learning python is the best"
print(unique_word_count(paragraph))
