"""
Most Common Word
Write a function most_common_word(text) that returns the word that
appears most frequently in a given paragraph. Ignore case. If multiple
words have the same count, return any one
"""


def most_common_word(text):
    words = text.lower().split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    return max(count, key=lambda w: count[w])


text = input("Enter text: ")
print(most_common_word(text))
