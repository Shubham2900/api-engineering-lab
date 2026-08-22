import time
from multiprocessing import Process


def cpu_work(n):
    total = 0

    for i in range(n):
        total += i

    return total


def main():
    start = time.time()

    processes = []

    for _ in range(5):
        process = Process(
            target=cpu_work,
            args=(50_000_000,),
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()