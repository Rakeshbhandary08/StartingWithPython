from concurrent.futures import ProcessPoolExecutor;
import time;
import asyncio;

# #create a cpu intensive task
# def intensive_work(name):
#     return name[::-1]

# async def main():
#     loop=asyncio.get_running_loop()
#     with ProcessPoolExecutor() as pool:
#         result=await loop.run_in_executor(pool,intensive_work,"Rakesh Bhandary")
#         print(result)

# if __name__ == "__main__":
#  asyncio.run(main())

#-------------------- another way ---------------------------

def calculate():
    total=0;
    for i in range(1000_00_00_0):
        total=total+i;
    

async def task1(pool):
    loop=asyncio.get_running_loop();
    await loop.run_in_executor(pool,calculate)
    print("Task1 is completed")

async def task2(pool):
    loop=asyncio.get_running_loop();
    await loop.run_in_executor(pool,calculate)
    print("Task2 is completed")

async def main():
     start=time.time()

     with ProcessPoolExecutor() as pool:
      await asyncio.gather(task1(pool),task2(pool))

     print("Total time taken",time.time()-start)

if __name__== "__main__":
 asyncio.run(main())