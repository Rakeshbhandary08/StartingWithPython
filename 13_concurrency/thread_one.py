# # import threading;
# # import time;

# # def serving_order(name,audi_no,seat_no,timing):
# #     print(f"Order is being taken by {name} for audi {audi_no} and seat {seat_no}\n")
# #     time.sleep(timing);
# #     print(f"Order is succesfully served by {name}")

# # #creating threads(workers)
# # t1=threading.Thread(target=serving_order,args=("Hritik",3,"B12",5))
# # t2=threading.Thread(target=serving_order,args=("Akash",5,"M10",3))

# # start=time.time()
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # end=time.time()

# # print(f"Order serving timing is {end-start:.0f} seconds")


# --------------- Challenge 1: Parallel File Downloader (Simulation)-------------
# # Difficulty: Easy
# # Problem statement
# # Imagine you are downloading 4 files from the internet.

# # Each file takes a different amount of time to download.

# # Your task is to use Python threading to download all four files concurrently(ek sath


# # Requirements
# # 1. Create a function download_file(filename, timing).
# # 2. Print Downloading {filename}... when downloading starts.
# # 3. Use time.sleep(timing) to simulate downloading.
# # 4. Print {filename} downloaded successfully! when completed.
# # 5. Create 4 threads, one for each file.
# # 6. Start all 4 threads.
# # 7. Use join() to ensure all downloads finish before printing All downloads completed!.
# # 8. Calculate the total execution time.

# import threading;
# import time;

# def download_file(filename,timing):
#     print(f"Downloading {filename}\n");
#     time.sleep(timing);
#     print(f"{filename} downloaded succesfully!\n")

# files=["rakesh.imp","script.js","style.css","index.html"]

# #Without threading
# # start=time.time()
# # for file in files:
# #     download_file(file,3)
# # end=time.time()

# #With threading
# start=time.time();
# threads=[]
# for file in files:
#     t=threading.Thread(target=download_file,args=(file,3))
#     t.start() #Thread has been started working
#     threads.append(t)

# for t in threads:
#     t.join()

# end=time.time()
# print(f"Time taken to download all files {end-start:.0f} seconds")


# ---------------------- Challenge 2: Multiple API Requests ---------------------------

# Imagine you're building a dashboard that needs information from 5 different APIs.

# Each API takes a different amount of time to respond.

# Your task:
# 1. Create a function fetch_data(api_name, timing).
# 2. Print Fetching data from {api_name}.
# 3. Simulate an API request using time.sleep(timing).
# 4. Print {api_name} data fetched successfully.
# 5. Create 5 threads dynamically using a loop.
# 6. Start all threads.
# 7. Use join() to wait for all API requests.
# 8. Calculate total execution time.

import threading;
import time;

def fetch_data(api_name,timing):
    print(f"Fetching data from {api_name}")
    time.sleep(timing)
    print(f"{api_name} data fetched successfully!")

apis=[("one",5),("two",2),("three","8"),("four",6),("five",1)]

#Create threads dynamically using loop
threads=[]
start=time.time()
for api in apis:
    t=threading.Thread(target=fetch_data,args=(api[0],int(api[1])));
    t.start()
    threads.append(t)

#make main thread wait for all the created threads
for t in threads:
    t.join()

end=time.time()

print(f"All the apis call has been succesfully fetched in {end-start:.0f} seconds")
