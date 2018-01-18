import thread
import time


# Define a function for the thread
def squre(n,delay):
    time.sleep(delay)
    print n*n
    return n*n

def qube(n,delay):
    time.sleep(delay)
    print n * n * n
    return n*n*n

# Create two threads as follows
try:
    a = thread.start_new_thread(squre,(5,5) )
    b = thread.start_new_thread(qube,(5,2))
    print a+b
except:
    print "Error: unable to start thread"

while 1:
    pass
