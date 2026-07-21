"""
Capitalize Long Words
Take a sentence as input. Capitalize only the first letter of each word
that is longer than 3 characters. Keep the rest as is.
"""

# sentence = input("Enter sentence: ")
# ans = sentence.capitalize()
# print(ans)


def capatalize_word(sentence: str):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) > 3:
            words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)


sentence = "vedant is a python dev"
print(capatalize_word(sentence))
