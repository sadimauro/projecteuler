#!/usr/bin/python3

import time
tStart = time.time()

def isPal(a):
    # transform a to pal(a)
    rem = a
    pal = 0
    while rem > 0:
        lowDig = rem % 10
        rem = rem // 10
        pal = 10*pal + lowDig

    # check if pal(a) == a
    return pal == a

biggestPal = 0

for a in range(100,1000):
    for b in range(100,1000):
        prod = a * b
        if isPal(prod):
            if prod > biggestPal:
                biggestPal = prod

print(biggestPal)
print("Run time: " + str((time.time() - tStart)))
