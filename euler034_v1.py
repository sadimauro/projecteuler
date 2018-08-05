#!/usr/bin/python3

import time
tStart = time.time()

import math

MAX_TO_TRY = 1000000000
bigSum = 0

for n in range(3,MAX_TO_TRY+1):
    temp = n
    factSum = 0
    while temp > 0:
        factSum += math.factorial(temp % 10)
        temp = temp // 10
    if n == factSum:
        bigSum += n
        print(n)

print(__file__ + ": answer: " + str(bigSum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
