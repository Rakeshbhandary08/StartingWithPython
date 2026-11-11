
import multiprocessing
import time

def count_counter():
    print("Process has been started")

    count = 0

    for i in range(1000_00_00_00):
        count += i

    print("Process has been ended")


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=count_counter)
    p2 = multiprocessing.Process(target=count_counter)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Time taken is {end-start:.2f} seconds")
