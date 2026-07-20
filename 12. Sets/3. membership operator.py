allowed_user = {"vedant", "vasu", "adi"}
user = input("Enter username: ")
if user in allowed_user:
    print("Access Granted")
else:
    print("Access Denied")
