#!/usr/bin/python3

import time
tStart = time.time()

import math
def isTrip(a,b,c):
    return math.pow(a,2) + math.pow(b,2) == math.pow(c,2)

for a in range(1,1000):
    for b in range(a,1000):
        if isTrip(a, b, 1000-b-a):
            print(__file__ + ": answer: " + str(a*b*(1000-b-a)))
            print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
            exit()
