import asyncio
import time


async def download_file(file_id):
    print(f"Starting download {file_id}")

    await asyncio.sleep(2)

    print(f"Finished download {file_id}")

async def monitor():
    for i in range(5):
        print(f"Monitor: {i}")
        await asyncio.sleep(0.5)

async def main():
    start = time.time()

    tasks = [
        download_file(i)
        for i in range(5)
    ]

    tasks.append(monitor())

    await asyncio.gather(*tasks)

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())