import numpy as np

def primes(n):
    sieve = np.ones(n//2, dtype = np.bool)
    sieve[0] = False

    for i in range(3, int(n**0.5)+1, 2):
        #need to convert index from full sieve to its half:
        #m = 2k+1 and k = //2
        if sieve[i//2]:
            sieve[(i**2)//2::i] = False
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
for i in range(t):
    m, n = input().split()
    pr = segmented_sieve(int(m), int(n))
    print(*pr, sep='\n')
    if i < t-1:
        print()
