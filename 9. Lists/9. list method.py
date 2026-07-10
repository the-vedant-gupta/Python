lst = ["Vedant", 22, 32.44, True, "Noida"]

print(lst, id(lst))

# lst.append(333)
# lst.append("Greater Noida")

# lst.insert(4, "Greater Noida")
# lst.insert(0, "Vasu")

# x = lst.pop(0) # By Index
# print(x)

lst.remove(22)  # By Value
print(lst)
