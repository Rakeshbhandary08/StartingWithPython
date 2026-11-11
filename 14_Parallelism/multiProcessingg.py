import multiprocessing
import time

def take_order():
    for i in range(1, 6):
        print(f"Taking order {i}")
        time.sleep(2)

def brew_order():
    for i in range(1, 6):
        print(f"Brewing order {i}")
        time.sleep(3)

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=take_order)
    p2 = multiprocessing.Process(target=brew_order)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process completed")