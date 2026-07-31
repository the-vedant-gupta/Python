try:
    num = int(input("Enter num: "))
    result = 100 / num
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(f"Result : {result:.2f}")
finally:
    print("Calcualtion attempt complete")
