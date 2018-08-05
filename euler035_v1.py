#!/usr/bin/python3

import time
tStart = time.time()

import stevepe

MAX_TO_TRY = 999999

def getShiftsSet(n):
    ret = set()
    nList = []
    while n > 0:
        nList.append(n % 10)
        n = n // 10
    lenNList = len(nList)
    for i in range(lenNList):
        newNum = 0
        for j in range(lenNList):
            newNum *= 10
            newNum += nList[(i+j)%lenNList]
        ret.add(newNum)
    return ret

count = 0
for n in range(2,MAX_TO_TRY+1):
    allPrimes = True
    for num in getShiftsSet(n):
        if not stevepe.isPrime(num):
            allPrimes = False
            break
    if allPrimes:
        count += 1
        
print(__file__ + ": answer: " + str(count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
