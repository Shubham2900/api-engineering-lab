import asyncio
import time


async def download_file(file_id):
    print(f"Starting download {file_id}")

    await asyncio.sleep(2)

    print(f"Finished download {file_id}")

    return f"File-{file_id}"


async def main():
    start = time.time()

    task1 = asyncio.create_task(download_file(1))
    task2 = asyncio.create_task(download_file(2))

    print("Tasks created")

    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())