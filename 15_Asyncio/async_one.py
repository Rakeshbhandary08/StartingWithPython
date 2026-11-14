import asyncio;
import time;

async def reading_books():
  print("Start reading book");
  await asyncio.sleep(2); #pause here,till run other tasks
  print("Reading is done")

start=time.time()
async def checking_books():
  await asyncio.gather(
    reading_books(), #async function
    reading_books(),
    reading_books()
  )

asyncio.run(checking_books())

end=time.time()

print(f"Total time taken is {end-start} seconds")