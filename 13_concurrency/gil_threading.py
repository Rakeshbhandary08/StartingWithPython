#GIL = Global Interpretor Lock
import threading;
import time;

def brew_Chai():
    print(f"{threading.current_thread().name} started brewing")
    count=0;
    for i in range(100_00_00_00):
        count=count + i;
    return count;

thread1=threading.Thread(target=brew_Chai,name="t1")
thread2=threading.Thread(target=brew_Chai,name="t2");

start=time.time()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

end=time.time()

print(f"Here is the time taken to Execute {end-start:.2f} seconds")