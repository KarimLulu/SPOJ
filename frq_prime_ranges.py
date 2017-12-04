import numpy as np

def primes(n):
    """Find primes numbers p < n"""
    sieve = np.ones(n//2, dtype=np.bool)
    limit = int(n ** 0.5)+1

    for p in range(3, limit, 2):
        if sieve[p//2]:
            sieve[(p**2)//2::p] = False

    return np.r_[2, 2*np.nonzero(sieve)[0][1:]+1]

def find_ranges(K, N):
    if K < 1:
        return N * (N - 1) // 2

    primeNums = primes(N+1)
    y = 0
    end = K - 1
    previous_prime = 1
    for prime in primeNums:
        if end < len(primeNums):
            count = prime - previous_prime
            y += (N - primeNums[end] + 1) * count
            end += 1
            previous_prime = prime
        else:
            break
    return y

for k in range(int(input())):
    N, K = input().split()
    print(find_ranges(int(K), int(N)))
