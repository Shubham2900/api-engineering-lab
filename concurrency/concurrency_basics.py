import time
from concurrent.futures import ThreadPoolExecutor


def download_file(file_id):
    print(f"Starting download {file_id}")

    time.sleep(2)

    print(f"Finished download {file_id}")

def cpu_work(n):
    total = 0

    for i in range(n):
        total += i

    return total


def main():
    # start = time.time()
    #
    # threads = []
    #
    # for i in range(5):
    #     thread = threading.Thread(
    #         target=cpu_work,
    #         args=(50_000_000,),
    #     )
    #
    #     threads.append(thread)
    #     thread.start()
    #
    # for thread in threads:
    #     thread.join()
    #
    # end = time.time()
    #
    # print(f"Total time: {end - start:.2f} seconds")

    # start = time.time()
    #
    # for _ in range(5):
    #     cpu_work(50_000_000)
    #
    # end = time.time()
    #
    # print(f"Total time: {end - start:.2f} seconds")

    start = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(download_file, i)
            for i in range(5)
        ]

        for future in futures:
            future.result()

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()