try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"num1/num2 = {num1/num2:.2f}")
# except ZeroDivisionError:
#     print("Can not divide by zero, please emter proper integers")
# except ValueError:
#     print("Please enter proper integers")
# except (ValueError, ZeroDivisionError):
#     print("Invalid Input. Try Again")
except Exception as e:
    # print("Some error occured")
    print(type(e).__name__)
    print(f"Error message = {e}")
