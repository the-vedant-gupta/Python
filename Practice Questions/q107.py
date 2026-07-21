"""
PAN Card Validation
Take a string as input. Check if it is a valid Indian PAN card number.
Format: 5 uppercase letters + 4 digits + 1 uppercase letter (Total 10
characters). Example: ABCDE1234F.

"""


def pancard_validate(pan: str):
    pan = pan.upper()
    if len(pan) != 10:
        return False
    if not pan[:5].isalpha():
        return False
    if not pan[5:9].isdigit():
        return False
    if not pan[9].isalpha():
        return False
    return True


pan = input("Enter pan No: ")
if pancard_validate(pan):
    print("Valid PAN")
else:
    print("Invalid PAN")
