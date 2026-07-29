"""
Create a class StringUtils with two static methods:
is_palindrome(s) and reverse_string(s).
No instance state needed.
"""


class StringUtils:

    @staticmethod
    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]

    @staticmethod
    def reverse_string(s):
        s = s.lower()
        return s[::-1]


print(StringUtils.is_palindrome("Madam"))
print(StringUtils.reverse_string("Madam"))
