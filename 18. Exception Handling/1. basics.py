try:
    age = int(input("Enter age:"))
    if age >= 18:
        print("Adult")
    else:
        print("Not Adult")
except:
    print("Some error occured")

print("Good")
