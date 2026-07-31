class InsufficientFundsError(Exception):
    pass


def withdraw_money(balance, witdhraw_amount):
    if witdhraw_amount > balance:
        raise InsufficientFundsError("Not Enough balance")
    print(f"Remaining balance= {balance - witdhraw_amount}")


try:
    withdraw_money(1000, 3000)
except InsufficientFundsError as e:
    print(f"Error name = {type(e).__name__}")
    print(f"error = {e}")
except Exception as e:
    print(f"Error name = {type(e).__name__}")
    print(f"error = {e}")
