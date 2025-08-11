import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate I/O delay
    print("Data fetched!")
    return {"data": 123}


async def main():
    task = asyncio.create_task(fetch_data())
    print("Doing other work...")
    await task  # Wait for task to complete
    print(f"Received data: {task.result()}")

asyncio.run(main())
