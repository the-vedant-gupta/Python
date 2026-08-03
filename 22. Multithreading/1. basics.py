import time
import threading


def task(name):
    print(f"{name} task is starting")
    time.sleep(2)
    print(f"{name} task is finished")


print("Main Program START\n")
t1 = threading.Thread(target=task, args=("cooking",))
t2 = threading.Thread(target=task, args=("baking",))
t1.start()
t2.start()

t1.join()
t2.join()

print("Main Program END")
