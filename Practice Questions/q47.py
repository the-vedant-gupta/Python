"""
Write a function power(base,exp) that returns base raised
to exp using a loop- no ** operator or pow() allowed
"""


def power(base, exp):
    result = 1
    for i in range(1, exp + 1):
        result *= base
    return result


pow = power(2, 10)
print(pow)
