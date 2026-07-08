# def square(num):
#     return num * num


square = lambda num: num * num

print(square(10))
# print(square(5))

# Return True if age >=18 else false


# def is_adult(age):
#     if age >= 18:
#         return True
#     return False


# print(is_adult(34))

is_adult = lambda age: True if age >= 18 else False

print(is_adult(34))
