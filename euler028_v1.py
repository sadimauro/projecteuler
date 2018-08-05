#!/usr/bin/python3

import time
tStart = time.time()

LAYERS = 501

sum = 1
lastNum = 1
for layer in range(2, LAYERS+1):
    for i in range(1,4+1):
        lastNum += (2*layer)-2
        sum += lastNum
        #print("lastNum = " + str(lastNum) + "; sum now = " + str(sum))

print(__file__ + ": answer: " + str(sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
