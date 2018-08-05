#!/usr/bin/python3

import time
tStart = time.time()

import math
def sumPD(n):
    """ return the sum of the proper divisors of n"""
    sum = 1
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            sum += i
            if i != (n // i):
                sum += (n // i)
    return sum

def isAbund(n):
    return sumPD(n) > n

def isDefic(n):
    return sumPD(n) < n

def isPerfect(n):
    return sumPD(n) == n

# First, collect all of the abundant numbers
MAX_TO_TRY = 28123
abunds = []
for n in range(1,MAX_TO_TRY+1):
    if isAbund(n):
        abunds.append(n)
print("len of abunds = " + str(len(abunds)))

# Next, find the sum
sumsOfTwoDict = {}
for i in range(1,MAX_TO_TRY+1):
    sumsOfTwoDict[i] = 0
for i in abunds:
    for j in abunds:
        if i+j <= MAX_TO_TRY:
            sumsOfTwoDict[i+j] = 1

sum = 0
for n in range(1,MAX_TO_TRY):
    if sumsOfTwoDict[n] == 0:
        sum += n

print(__file__ + ": answer: " + str(sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
