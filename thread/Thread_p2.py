import time
import threading

balance = 0
lock = threading.Lock()


def change_it(t):
    global balance
    balance += t
    balance -= t


def run_thread(n):
    for x in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


thread = threading.Thread(target=run_thread, name='loop_thread', args=(5,))
thread1 = threading.Thread(target=run_thread, name='loop_thread', args=(8,))
thread.start()
thread1.start()
thread.join()
thread1.join()
print(balance)
