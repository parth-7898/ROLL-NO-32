import threading
import time


def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", letter)
        time.sleep(1)


def display_messages():
    for i in range(1, 6):
        print("Message:", i)
        time.sleep(1)


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=display_messages)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed.")
