try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"num1/num2 = {num1/num2:.2f}")
# except ZeroDivisionError:
#     print("Can not divide by zero, please emter proper integers")
# except ValueError:
#     print("Please enter proper integers")
except (ValueError, ZeroDivisionError):
    print("Invalid Input. Try Again")
except:
    print("Some error occured")
