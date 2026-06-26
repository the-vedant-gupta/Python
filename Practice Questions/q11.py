"""
Take a person's age and whether they have a valid ID(True/False)as input.
They can enter a venue if they are 18 or older AND have a valid ID. Print the appropriate message.
"""

person_age = int(input("Enter your age= "))
valid_id = input("Do you have a valid ID ? (True/False): ") == "True"
if person_age >= 18 and valid_id:
    print("You are elegible to enter the venue")
else:
    print("You are not elegible to enter the venue")
