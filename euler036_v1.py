#!/usr/bin/python3

import time
tStart = time.time()

MAX_TO_TRY = 999999
sumAll = 0

for n in range(MAX_TO_TRY+1):
    decStr = str(n)
    if decStr != decStr[::-1]:
        continue
    binStr = format(n, 'b')
    if binStr != binStr[::-1]:
        continue
    sumAll += n

print(__file__ + ": answer: " + str(sumAll))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
