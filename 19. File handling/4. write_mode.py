with open("new.txt", "w") as f:
    f.write("Hey guys\n")
    f.write("Good bye\n")

lines = ["hey\n", "hello\n", "how are you\n"]
with open("new.txt", "w") as f:
    f.writelines(lines)
