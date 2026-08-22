import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def worker_1():
    print("Worker 1: acquiring Lock A")
    with lock_a:
        print("Worker 1: acquired Lock A")

        time.sleep(1)

        print("Worker 1: waiting for Lock B")
        with lock_b:
            print("Worker 1: acquired Lock B")


def worker_2():
    print("Worker 2: acquiring Lock B")
    with lock_b:
        print("Worker 2: acquired Lock B")

        time.sleep(1)

        print("Worker 2: waiting for Lock A")
        with lock_a:
            print("Worker 2: acquired Lock A")


thread_1 = threading.Thread(target=worker_1)
thread_2 = threading.Thread(target=worker_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Done")