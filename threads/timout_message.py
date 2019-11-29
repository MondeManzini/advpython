#!/usr/bin/env python
from threading import Thread
from time import sleep


def timeout_message(message=None, repeat=3, timeout=5):
    def target(x=None):
        for i in range(repeat):
            sleep(timeout)
            print '\n'+message + str(x)

    t = Thread(target=target, args=(10,))
    t.setDaemon(1)
    t.start()
    raw_input('Press Enter when done')


timeout_message('hello')
