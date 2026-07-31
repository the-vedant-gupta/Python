def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative")
        elif age >= 150:
            print("Age is not real")
    except ValueError as e:
        print(f"Inside fn error: {e}")
        raise
    except Exception as e:
        print(f"Inside function Error: {e}")


try:
    check_age()
except Exception as e:
    print(f"Outside error: {e}")
else:
    print("Success")
