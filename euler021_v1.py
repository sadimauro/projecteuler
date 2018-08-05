#!/usr/bin/python3

import time
tStart = time.time()

sum = 0
MAX = 9999

import math
def calcProperDivsSum(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum

d = []
for i in range(0,MAX+1):
    d.append(0)

for i in range(1,MAX+1):
    d[i] = calcProperDivsSum(i)
    #print("i = " + str(i) + "; properDivsSum = " + str(d[i]))
    if d[i] <= MAX and d[i] != i and d[d[i]] == i:
        print("found an amicable pair! " + str(i) + " and " + str(d[i]))
        sum += i
        sum += d[i]

print(__file__ + ": answer: " + str(sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
