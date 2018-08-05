#!/usr/bin/python3

import time
tStart = time.time()

import math

maxSolns = 0
maxSolnsP = 0
for p in range(1, 1001):
    # count number of solutions for this p value.
    thisNumSolns = 0
    for sideA in range(1,p):
        for sideB in range(1,p-sideA):
            sideC = math.sqrt((sideA**2) + (sideB**2))
            if sideA + sideB + sideC == p:
                #print("found a solution! {}, {}, {}".format(str(sideA), str(sideB), str(sideC)))
                thisNumSolns += 1

    # check max
    #print("this num solutions = {!s}".format(thisNumSolns))
    if thisNumSolns > maxSolns:
        maxSolns = thisNumSolns
        maxSolnsP = p

print(__file__ + ": answer: " + str(maxSolnsP))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
