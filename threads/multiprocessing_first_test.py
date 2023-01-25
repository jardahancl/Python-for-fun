import time
from multiprocessing import Process, Value, Array, Lock


def add100r(number, numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1
            for i in range(len(numbers)):
                numbers[i] += 1



if __name__ == '__main__':
    print('start main')

    shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 1.25, 0.00014, 200.2])
    lock = Lock()
    print(f'Number at beginning {shared_number.value}')
    print(f'Array at beginning {shared_array[:]}')

    p1 = Process(target=add100r, args=(shared_number, shared_array, lock))
    p2 = Process(target=add100r, args=(shared_number, shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Number at the end is {shared_number.value}')
    print(f'Array at the end is {shared_array[:]}')


    print('end main')