import threading

local_std = threading.local()


def get_proess_std():
    std = local_std.student
    print('hello %s (in %s)' % (std, threading.currentThread().name))


def run_thread(name):
    local_std.student = name;
    get_proess_std()


thread1 = threading.Thread(target=run_thread, name='thread1', args=('kevin',))
thread2 = threading.Thread(target=run_thread, name='thread2', args=('doubleMine',))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
