import time

print("second")


def runsecond():
    print("second file")
    for i in range(0, 25):
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    runsecond()
