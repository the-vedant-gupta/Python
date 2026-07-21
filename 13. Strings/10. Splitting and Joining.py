"""
split() : Break String into List
join() : Combine List into String
"""

# text = "vedant gupta is a coder"
# print(text.split())

my_list = ["v", "e", "d", "a", "n", "t", 5]
ans = "".join(str(ch) for ch in my_list)
print(ans)
print(type(ans))
