import asyncio

async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)  # Simulate an async I/O-bound task
    print(f"{name} finished")

async def main():
    tasks = [
        worker(name=f"Worker-{i}", delay=i) for i in range(3)
    ]
    await asyncio.gather(*tasks)  # Run all tasks concurrently

asyncio.run(main())
