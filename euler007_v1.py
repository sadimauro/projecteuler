#!/usr/bin/python3

import time
tStart = time.time()

import math

def isPrime(a):
    for i in range(3, math.floor(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True

MAX_COUNT = 10001

# Count '2' as a prime (count = 1), and
# start with testNum = 1 so that the first
# iteration will be = 3.
testNum = 1
count = 1
while count < MAX_COUNT:
    testNum += 2
    if isPrime(testNum):
        count += 1
        
print("Answer: " + str(testNum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
