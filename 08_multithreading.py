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


timer()

# Asynchronous calls

class AsyncWrite(Thread):
    def __init__(self, text, out):
        super().__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)

