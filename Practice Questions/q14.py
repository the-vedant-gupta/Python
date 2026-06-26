"""
A shop gives discounts based on purchase amount:
above 5000 --> 20% discount
above 2000 --> 10% discount
above 1000 --> 5% discount
1000 or below --> no discount
"""

purchased_amount = int(input("Enter the amount= "))

# if purchased_amount >= 5000:
#     net_amount = (purchased_amount / 100) * 80
#     print(
#         f"Your total amount is {purchased_amount} after getting 20% discount you net amount is {net_amount}"
#     )
# elif purchased_amount >= 2000:
#     net_amount = (purchased_amount / 100) * 90
#     print(
#         f"Your total amount is {purchased_amount} after getting 20% discount you net amount is {net_amount}"
#     )
# elif purchased_amount >= 1000:
#     net_amount = (purchased_amount / 100) * 95
#     print(
#         f"Your total amount is {purchased_amount} after getting 20% discount you net amount is {net_amount}"
#     )
# else:
#     print(f"You total amount is {purchased_amount}")


discount = (
    20
    if purchased_amount >= 5000
    else 10 if purchased_amount >= 2000 else 5 if purchased_amount >= 1000 else 0
)

net_amount = purchased_amount * (100 - discount) / 100

print(f"Total Amount: {purchased_amount}")
print(f"Discount: {discount}")
print(f"Net Amount: {net_amount}")
