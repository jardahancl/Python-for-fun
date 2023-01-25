from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=worker, args=(q, lock))
        t.deamon=False
        t.start()

    for i in range(21):
        q.put(i)

    q.join()

    print('end main')