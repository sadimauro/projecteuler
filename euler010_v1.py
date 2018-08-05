#!/usr/bin/python3

import time
tStart = time.time()

import math
def isPrime(a):
    for i in range(3, math.floor(math.sqrt(a))+1, 2):
        if a % i == 0:
            return False
    return True

sum = 2
for i in range(3,2000000,2):
    if isPrime(i):
        sum += i

print(__file__ + ": answer: " + str(sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
