import threading;
import time;

def take_order():
    for i in range(1,6):
        print(f"Taking order for orderId {i}")
        time.sleep(2)

def brew_order():
    for i in range(1,6):
        print(f"Brewing orderId {i}");
        time.sleep(3)


#create thread
takingOrder=threading.Thread(target=take_order)
brewingOrder=threading.Thread(target=brew_order)

takingOrder.start();
brewingOrder.start();

#wait to finish these two thread
takingOrder.join();
brewingOrder.join();

print("Main thread completed")