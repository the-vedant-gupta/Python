"""
Clean Phone Number
Take a phone number as input in the format +91-98765-43210.
Remove all dashes and the country code. Print the cleaned 10-digit
number.

"""


def clean_no(phone_no: str):
    if phone_no.startswith("+"):
        phone_no = phone_no.split("-", 1)[1]
        phone_no = phone_no.replace("-", "")
        phone_no = phone_no.replace("+", "")
    return phone_no


phone_no = "+34-32534-52345"
print(clean_no(phone_no))
