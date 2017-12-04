import numpy as np
from sys import stdout

def primes(n):
    """Find primes numbers p < n"""
    sieve = np.ones(n//2, dtype=np.bool)
    sieve[0] = False #mark 1 as not prime
    limit = int(n ** 0.5)+1
    for p in range(3, limit, 2):
        #convert indexing on the full sieve to the indexing on its half
        # m = 2k + 1 and k = m//2
        if sieve[p//2]:
            sieve[(p**2)//2::p] = False
    return np.r_[2, 2*np.nonzero(sieve)[0]+1]

def segmented_sieve(m, n):
    primeN = primes(int(n**0.5)+1)
    sieve = np.ones(n-m+1, dtype=np.bool)
    for prime in primeN:
        start = max(2, ((m+prime-1)//prime)) * prime - m
        sieve[start::prime] = False
    if m > 1:
        return np.nonzero(sieve)[0]+m
    else:
        return np.nonzero(sieve)[0][1:]+m


t = int(input())
for k in range(t):
    m, n = input().split()
    p = segmented_sieve(int(m), int(n))
    stdout.write('\n'.join(p.astype(str))+'\n')
