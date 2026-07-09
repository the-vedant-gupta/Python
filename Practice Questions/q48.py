"""
Write  a function tax_calculation(income) that takes annual income
and returns the tax amount based on these slabs:

Upto to 2,50,000 -> No tax
2,50,000 to 5,00,000 -> 5%
5,00,000 to 10,00,000 -> 20%
above 10,00,000 -> 30%
"""

# def tax_calculation(income):
#     if income <= 250000:
#         return "No tax"
#     elif income > 250000 and income <= 500000:
#         tax = (5 / 100) * income
#         return f"tax amount is {tax}"
#     elif income > 500000 and income <= 1000000:
#         tax = (20 / 100) * income
#         return f"tax amount is {tax}"
#     elif income > 1000000:
#         tax = (30 / 100) * income
#         return f"tax amount is {tax}"


# new_amount = tax_calculation(3400000)
# print(new_amount)


def tax_calculation(income):

    if income <= 250000:
        return 0

    elif income <= 500000:
        return income * 5 / 100

    elif income <= 1000000:
        return income * 20 / 100

    else:
        return income * 30 / 100


income = float(input("Enter your annual income: "))

tax = tax_calculation(income)

print("Tax Amount =", tax)
