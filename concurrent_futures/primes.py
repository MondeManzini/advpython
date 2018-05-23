from concurrent.futures import ProcessPoolExecutor 

def genprimes(n):
    primes=[2]
    for i in range(2,n+1):                                                                              
        for p in primes:
            if i%p==0:break
        else: primes.append(i)
    return primes

def genprimes2(n):
    primes = reduce(
             lambda x,y:x if len(filter(lambda a:y%a==0, x))>0 else x + (y,),
             [(2,)]+range(3,n+1))
    return primes
    
p1 = ProcessPoolExecutor().submit(genprimes,500)
p2 = ProcessPoolExecutor().submit(genprimes2,500)

print "\033[91m P1",p1.result(),"\033[00m"
print "P2",p2.result()

