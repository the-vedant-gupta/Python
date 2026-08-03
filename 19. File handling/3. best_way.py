try:
    with open("hello.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File does not exist")
except:
    print("Some error occured")
