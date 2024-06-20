# a flow of execution
import multithreading
import time

#def study():
 #   time.sleep(5)
 #   print("you finish studying")

#def eat():
 #   time.sleep(3)
 #   print("you are full")

#  x.threading.Thread(target= study, args=())
#  x.start()

#  y.threading.Thread(target= eat, args=())
#  y.start()

# join()--waits for a thread to finish to synchronize and join
# before it moves on to instruction set

#  print(threading.active_count()) # thread counts
#  print(threading.enumerate)  # list of threads that are running
#  print(time.perf_counter())  # how long it takes the thread to finish


# daemon thread--runs in the background
# used in ex. background tasks, garbage collection, waiting for input, long running processes

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('logged in for: ', count, 'seconds')

x = threading.Thread(target= timer, daemon= True)
x.start()

#  x.setDaemon(True)
#  print(x.isDaemon()) # checks if a thread is a daemon or not

answer = input('do you wish to exit?')
