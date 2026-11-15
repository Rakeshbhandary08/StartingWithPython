import asyncio;
from concurrent.futures import ThreadPoolExecutor
import time;

#Create a blocking function that blocks the main thread
def blocking_main():
    print("Start blocking the main thread...");
    time.sleep(5)
    print("Blocking has been done, UnBlock");

async def another_task():
    for i in range(5):
        print("Main thread is running :",i);
        await asyncio.sleep(1)



async def main():
     loop=asyncio.get_running_loop()
     with ThreadPoolExecutor() as pool:
       task1=loop.run_in_executor(pool,blocking_main) #another thread with same event loop
       task2=asyncio.create_task(another_task()) #another task

       await asyncio.gather(task1,task2)

asyncio.run(main())

