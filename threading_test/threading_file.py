import threading
import time


def sing():
    for i in range(3):
        print("sing...")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("dance...")
        time.sleep(0.5)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    sing_thread.start()
    dance_thread.start()
