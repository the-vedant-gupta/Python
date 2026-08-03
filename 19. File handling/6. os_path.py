import os

print(os.path.exists("hello.txt"))


print(os.path.isfile("hello.txt"))
print(os.path.isdir("hello.txt"))

print(os.path.getsize("hello.txt"))

path = os.path.join("data", "logs", "apps.log")
print(path)


## Pathlib

from pathlib import Path

file_path = Path("hello.txt")

print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())
print(file_path.stat().st_size)  # this gives an eror if file isn't exist
