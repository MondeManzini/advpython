def genprimes(n,primes=[2]):
    yield 1
    for j in primes:
        yield j
        if j == n: 
            break
    for i in xrange(j+1,n+1):
        for p in primes:
            if i%p == 0: 
                break
        else: 
            primes.append(i)
            yield i

def genprimes2(n,primes=[2]):
    yield 1
    for j in primes:
        yield j
        if j == n: 
            break
    for i in xrange(j+1,n+1):
        for p in primes:
            if i%p == 0: 
                break
        else: 
            primes.append(i)
            yield i

if __name__ == '__main__':
    for i in genprimes(99999): print i
