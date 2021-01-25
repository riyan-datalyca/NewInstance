import second as s
from third import Third
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import threading
print("main file")
print(os.cpu_count())
print()

def runmain():
    for i in range(0, 25):
        print(i)

t = Third()
s.runsecond()
t.runthird()
# t1 = threading.Thread()
# t2 = threading.Thread()
# t2.start()
# t1.start()
# t1.run(runmain())
# t2.run(s.runsecond())
#
# t1.join()
# t2.join()
print(threading.activeCount())