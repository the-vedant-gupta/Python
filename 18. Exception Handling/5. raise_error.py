def set_age(age: int):
    if age < 0:
        raise ValueError("Age cannnot be negative")
    elif age >= 150:
        raise ValueError("Age is not real")
    print("Your age is corect")


try:
    set_age(1000)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
