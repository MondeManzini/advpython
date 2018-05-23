from threading import Thread, local
from Queue import Queue
from time import sleep

printq = Queue()
def loop_nos():
    printq.put("Starting P1")
    for i in xrange(10):
        sleep(1)
        printq.put(str(i))

def loop_chars():
    printq.put("Starting P2")
    for j in xrange(65,76):
        sleep(1)
        printq.put(chr(j))

def printer():
    while True:
        out = printq.get()
        if out is None:
            break
        print out


printq.put('startup')
t1 = Thread(target=loop_chars)
t1.start()
t2 = Thread(target=loop_nos)
t2.start()
t3= Thread(target=printer)
t3.start()
Thread.join(t1)
Thread.join(t2)
printq.put(None)
Thread.join(t3)
print "done", printq
