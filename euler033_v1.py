#!/usr/bin/python3

import time
tStart = time.time()

import math

def getOnes(n):
    return n // 10

def getTens(n):
    return n % 10

def curiousReduce(num, denom):
    onesNum = getOnes(num)
    tensNum = getTens(num)
    onesDenom = getOnes(denom)
    tensDenom = getTens(denom)

    if tensDenom != 0 and tensNum == onesDenom:
        return (onesNum, tensDenom)

    if onesDenom != 0 and onesNum == tensDenom:
        return (tensNum, onesDenom)

    return (num, denom)

nonTrivials = []
for num in range(10,100):
    for denom in range(num+1,100):
        (crNum, crDenom) = curiousReduce(num, denom)
        if crNum != num and crDenom != denom:
            if crNum / crDenom == num / denom:
                nonTrivials.append((num,denom))

print(nonTrivials)

numProd = 1
denomProd = 1
for i in range(len(nonTrivials)):
    numProd *= nonTrivials[i][0]
    denomProd *= nonTrivials[i][1]

print(__file__ + ": answer: " + str(denomProd//math.gcd(numProd,denomProd)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
