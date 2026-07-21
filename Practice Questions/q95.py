"""
Email Validation
Take an email as input. Validate that it contains exactly one @ and at
least one.. Print "Valid" or "Invalid".
"""


def check_email(email):
    if email.count("@") == 1 and "." in email:
        return "Valid"
    return "Invalid"


email = input("Enter email: ")
print(check_email(email))
