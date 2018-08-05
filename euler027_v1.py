#!/usr/bin/python3

import time
tStart = time.time()

from stevepe import isPrime

def countConsecQuadPrimes(a, b):
    n = 0
    while True:
        if not isPrime((n ** 2) + (a * n) + b):
            return n
        n += 1

maxConsecQuadPrimes = 0
productCoeffsAtMaxConsecQuadPrimes = 0

for a in range(-999,1000):
    for b in range(-1000, 1001):
        thisCount = countConsecQuadPrimes(a, b)
        if thisCount > maxConsecQuadPrimes:
            print("this count = " + str(thisCount))
            print("coeffs = " + str(a) + ", " + str(b))
            maxConsecQuadPrimes = thisCount
            productCoeffsAtMaxConsecQuadPrimes = a * b

print(__file__ + ": answer: " + str(productCoeffsAtMaxConsecQuadPrimes))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
