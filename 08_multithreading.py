from threading import Thread
import time

# Simple demonstration of multithreading.
def time_counter(name, delay, repeat) :
    print("Timer:", name, "started.")
    while repeat > 0:
        time.sleep(delay)
        print(name, ":", str(time.ctime(time.time())))
        repeat -= 1

    print("Timer:", name, "completed.")

def timer():
    t1 = Thread(target=time_counter, args=("Timer1", 1, 5))
    t2 = Thread(target=time_counter, args=("Timer2", 2, 5))
    t3 = Thread(target=time_counter, args=("Timer3", 3, 5))

    t1.start()
    t2.start()
    t3.start()

    print("Timer completed!")


# timer()

# Asynchronous calls

class AsyncWrite(Thread):
    def __init__(self, text, out):
        # super().__init__(self)
        Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)
        print("Finished writing to file :", self.out)


message = input("Message to write to file :\n")
background = AsyncWrite(message, "asyncwriteout.txt")
background.start()
print("The program can continue!")
for i in range(100):
    print(i)

background.join()
print("Waited until thread was complete.")

print("= = = = = = = = = = = = = = = = = = = = = = = = =")

# LOCKS
# Let us modify our Timer program to demonstrate a simple use of locks
import threading

tLock = threading.Lock()

def time_counter_l(name, delay, repeat) :
    print("Timer:", name, "started.")

    tLock.acquire()
    print(name, "acquired lock.")

    while repeat > 0:
        time.sleep(delay)
        print(name, ":", str(time.ctime(time.time())))
        repeat -= 1

    print(name, "is releasing the lock.")
    tLock.release()
    print("Timer:", name, "completed.")

def timer_l():
    t1 = threading.Thread(target=time_counter_l, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=time_counter_l, args=("Timer2", 2, 5))
    t3 = threading.Thread(target=time_counter_l, args=("Timer3", 3, 5))

    t1.start()
    t2.start()
    t3.start()

    print("Timer completed!")

timer_l()

# Semaphore. Check out semaphores.
