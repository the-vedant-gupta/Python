# 1 to 20, but only even numbers

# new_lst = [i for i in range(1, 11) if i % 2 == 0]
# new_lst = [i for i in range(1, 101) if i % 3 == 0 and i % 7 == 0]
# print(new_lst)

# From 1 to 100, make a list of all prime numebrs


def is_prime(num):
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    return False


new_lst = [i for i in range(2, 100) if is_prime(i) == True]
print(new_lst)
