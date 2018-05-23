import multiprocessing as mp
import os
import time
printq = mp.Queue()

def genprimes(n):
    primes=[2]
    for i in range(2,n+1):                                                                              
        for p in primes:
            if i%p==0:break
        else: primes.append(i)
    printq.put("\033[91m P1"+ str(primes) + "\033[00m")

def genprimes2(n):
    primes = reduce(
             lambda x,y:x if len(filter(lambda a:y%a==0, x))>0 else x + (y,),
             [(2,)]+range(3,n+1))
    printq.put("P2"+str(primes))

if __name__ == '__main__':

    start = time.time()
    genprimes(30000)
    genprimes2(30000)
    normaltime =  time.time() - start
    start = time.time()
    jobs = []
    for fn in [genprimes,genprimes2]:
        p = mp.Process(target=fn, args=(30000,))
        jobs.append(p)
        p.start()
    for p in jobs:
        p.join()
    while not printq.empty():
        printq.get()
    print '-'*80
    print 'time', time.time() - start
    print 'normaltime', normaltime
