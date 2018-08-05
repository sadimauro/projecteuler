#!/usr/bin/python3

import time
tStart = time.time()

def fifthPowerSum(n):
    thisSum = 0
    while n > 0:
        thisSum += (n % 10)**5
        n = n // 10
    return thisSum

MAX_TO_TRY = 2000000

fifthPowerSumsSet = set()
for n in range(2,MAX_TO_TRY+1):
    if n == fifthPowerSum(n):
        print("found one! n = " + str(n))
        fifthPowerSumsSet.add(n)

overallSum = 0
for n in fifthPowerSumsSet:
    overallSum += n

print(__file__ + ": answer: " + str(overallSum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
