import threading
import time


def loop():
    print('thread %s is running....' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('current thread %s >>> %s' % (threading.currentThread().name, n))
        time.sleep(1)
        print('thread %s is ended' % threading.currentThread().name)
print('thread %s is started ' % threading.currentThread().name)
t = threading.Thread(target=loop, name='loopThread')
t.start()
t.join()
print('thread %s is finish' % threading.currentThread().name)
