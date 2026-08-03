import os
from pathlib import Path

# os.mkdir("new_folder")
# Path("new_folder").mkdir()

# os.remove("neww.txt")
# Path("neww.txt").unlink()

# os.rename("new.txt", "Neww.txt")
# Path("new.txt").rename("neww.txt")

# for f in os.listdir("."):
#     print(f)

for f in Path(".").iterdir():
    print(f)
