#!/usr/bin/python3

import time
tStart = time.time()

import math

def truncateFromRight(n):
    ret = set()
    temp = n // 10
    while temp > 0:
        ret.add(temp)
        temp = temp // 10
    #print("right truncations = " + str(ret))
    return ret

def truncateFromLeft(n):
    ret = set()
    i = 1
    for thisPow in range(math.floor(math.log(n,10))):
        temp = n % (10**(thisPow+1))
        ret.add(temp)
    #print("left truncations = " + str(ret))
    return ret

import stevepe
n = 9
count = 0
allSum = 0
while count < 11:
    n += 2
    possiblyPrime = True
    if not stevepe.isPrime(n):
        possiblyPrime = False
        next
    for possPrime in truncateFromRight(n):
        if not stevepe.isPrime(possPrime):
            possiblyPrime = False
            break
    for possPrime in truncateFromLeft(n):
        if not stevepe.isPrime(possPrime):
            possiblyPrime = False
            break
    if possiblyPrime:
        print("Found a truncatable prime! = " + str(n))
        count += 1
        allSum += n

print(__file__ + ": answer: " + str(allSum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
