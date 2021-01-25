import time
import os
import threading

print("main file")
print(os.cpu_count())
print()

def runmain():
    for i in range(0, 25):
        print(i)


os.startfile("second.exe")
time.sleep(10)
