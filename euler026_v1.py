#!/usr/bin/python3

import time
tStart = time.time()

N_TO_TRY = 1000
CYCLES_TO_TRY = 1000
import decimal

longestCycleLen = 0
longestCycleD = 0
for d in range(1,N_TO_TRY+1):
    decimal.getcontext().prec = d
    a = decimal.Decimal(1) / decimal.Decimal(d)
    print("d = " + str(d) + "; a = " + str(a))
    
    #if this is finite, skip it
    if len(str(a)) < d:
        continue

    for cycleLen in range(1,CYCLES_TO_TRY):#d-1):
        a = decimal.Decimal(1) * ((10**cycleLen) - 1) / decimal.Decimal(d)
        #print("cycleLen = " + str(cycleLen) + "; a = " + str(a))
        if len(str(a)) < d:
            print("found a repeat; cycleLen = " + str(cycleLen))
            if cycleLen > longestCycleLen:
                print("new long cycleLen")
                longestCycleLen = cycleLen
                longestCycleD = d
            break

print(__file__ + ": answer: " + str(longestCycleD))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
