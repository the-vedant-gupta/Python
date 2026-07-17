my_tupels = (53, 22, "Vedant", "Vasu", "Greater Noida")

n = len(my_tupels)
for i in range(0, n):
    print(my_tupels[i], end=" ")

print()
for ele in my_tupels:
    print(ele, end=" ")

print()
for index, value in enumerate(my_tupels):
    print(f"Index = {index} and value = {value}")
