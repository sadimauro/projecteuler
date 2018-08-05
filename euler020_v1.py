#!/usr/bin/python3

import time
tStart = time.time()

def addDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

import math
print(__file__ + ": answer: " + str(addDigits(math.factorial(100))))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
