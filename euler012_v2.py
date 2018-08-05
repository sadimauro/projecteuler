#!/usr/bin/python3

import time
tStart = time.time()

MAX_DIVISORS = 500

def tri(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

import math
def countDivisors(n):
    numDivs = 0
    # check all numbers less than the sqrt
    for i in range(1,math.ceil(math.sqrt(n))):
        if n % i == 0:
            numDivs += 2
    # then check sqrt
    if n % math.sqrt(n) == 0:
        numDivs += 1
    return numDivs

thisTri = 0
j = 0
while True:
    j += 1
    thisTri += j
    if countDivisors(thisTri) > MAX_DIVISORS:
        break

print(__file__ + ": answer: " + str(tri(j)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
