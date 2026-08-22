import threading, time

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(100_000):
        with lock:
            current = counter
            time.sleep(0)
            current += 1
            counter = current


threads = []

for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Expected:", 500_000)
print("Actual:", counter)