#!/usr/bin/python3

import time
tStart = time.time()

import stevepe

largestPan = 0
for n in range(3, 987654321+1, 2):
    if stevepe.isIntPandigital(n):
        if stevepe.isPrime(n):
            if n > largestPan:
                largestPan = n

print(__file__ + ": answer: {!s}".format(largestPan))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
