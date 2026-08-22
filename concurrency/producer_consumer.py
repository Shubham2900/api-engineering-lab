import threading
import time
from queue import Queue

queue = Queue()


def producer():
    for i in range(10):
        print(f"Producing: {i}")
        queue.put(i)
        time.sleep(0.5)

    queue.put(None)


def consumer():
    while True:
        item = queue.get()

        if item is None:
            queue.task_done()
            break

        print(f"Consuming: {item}")
        time.sleep(1)

        queue.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Done")