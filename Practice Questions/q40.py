"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""


def discount_price(original_price, discount_percent):
    discount_amount = (discount_percent / 100) * original_price
    final_price = original_price - discount_amount
    # final_price = original_price - (discount_percent / 100) * original_price
    print(f"You will get discount of Rs. {discount_amount}")
    print(f"Yout fianl amount is : {final_price}")


discount_price(100, 10)
discount_price(6546, 65)
