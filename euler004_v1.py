#!/usr/bin/python3

import time
tStart = time.time()

biggestPal = 0

for a in range(100,1000):
    for b in range(100,1000):
        prod = a * b
        if str(prod) == str(prod)[::-1]:
            if prod > biggestPal:
                biggestPal = prod

print(biggestPal)
print("Run time: " + str((time.time() - tStart)))
