#!/usr/bin/python3

import time
tStart = time.time()

import stevepe
import itertools

STR = "123456789"

largestPan = 0
for nLen in range(9, 1, -1):
    for tup in itertools.permutations(STR[0:nLen]):
        n = stevepe.tupleToInt(tup)
        if stevepe.isPrime(n):
            if stevepe.isIntPandigital(n):
                if n > largestPan:
                    largestPan = n
    if largestPan > 0:
        break

print(__file__ + ": answer: {!s}".format(largestPan))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
