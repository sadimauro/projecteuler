#!/usr/bin/python3

import time
tStart = time.time()

import math
idx = 3
i = 1
j = 1
k = 0
while True:
    k = i + j
    if math.log(k,10) >= (1000-1):
        break
    i = j
    j = k
    idx += 1

print(__file__ + ": answer: " + str(idx))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
