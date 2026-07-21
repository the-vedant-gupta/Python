"""
Longest Word
Take a sentence as input. Print the longest word in it
"""


def longesst_word(sentence: str):
    words = sentence.split()
    print(max(words, key=lambda x: len(x)))
    # longest_count = 0
    # longest_word = ""
    # for word in words:
    #     if len(word) > longest_count:
    #         longest_count = len(word)
    #         longesst_word = word
    # print(longesst_word)


sentece = "Vedant is a prgrammer"
longesst_word(sentece)
