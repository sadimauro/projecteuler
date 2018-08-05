#!/usr/bin/python3

import time
tStart = time.time()

import math
def calcRoutes(m,n):
    return int(math.factorial(m+n) / (math.factorial(m) * math.factorial(n)))

#for i in range(1,20):
#    print(str(i) + " -> " + str(calcRoutes(i,i)))

print(__file__ + ": answer: " + str(calcRoutes(20,20)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
