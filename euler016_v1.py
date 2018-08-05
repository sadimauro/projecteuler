#!/usr/bin/python3

import time
tStart = time.time()

bigNum = 2**1000
mySum = 0
while bigNum > 0:
    mySum += (bigNum % 10)
    bigNum = bigNum // 10

print(__file__ + ": answer: " + str(mySum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
