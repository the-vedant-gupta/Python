"""
Username Validation
Take a username as input. Strip any spaces from both sides and check
if the cleaned name starts with a letter (not a digit). Print "Valid" or
"Invalid"
"""


def input_validation(username: str):
    username = username.strip()
    if username[0].isdigit():
        return "Invalid"
    return "Valid"


username = "Vedant"
print(input_validation(username))
