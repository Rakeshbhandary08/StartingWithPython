import asyncio;
import aiohttp;
import time;

async def main(delay):
    async with aiohttp.ClientSession() as session:
        print("Networking calling started")
        async with session.get(f"https://httpbin.org/delay/{delay}") as response:
            print("status",response.status)
            data=await response.json()
            print(data)

start=time.time()

asyncio.run(main(5))
end=time.time()

print(f"Total time {end-start} seconds")