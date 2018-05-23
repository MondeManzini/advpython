from time import sleep

def loop_nos():
    print("Starting P1")
    for i in xrange(10):
        sleep(0.5)
        print(str(i))
        yield

def loop_chars():
    print("Starting P2")
    for j in xrange(65,76):
        sleep(0.5)
        print(chr(j))
        yield

nos = loop_nos()
chars = loop_chars()

for i in xrange(10):
    next(nos)
    next(chars)
