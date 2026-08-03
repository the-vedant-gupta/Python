def addition(a: int, b: int) -> int:
    return a + b


def substraction(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    return a / b


PI = 3.14  # The value of that variable can't be changed

if __name__ == "__main__":
    print(f"Calculator file name= {__name__}")
    print("Testing this code")
    result = addition(10, 20)
    print(result)
