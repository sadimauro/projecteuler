#!/usr/bin/python3

import time
tStart = time.time()

def calcRoutes(m,n):
    if m == 1 or n == 1:
        return m + n
    elif m == n:
        return 2 * calcRoutes(m-1,n)
    else:
        return calcRoutes(m-1,n) + calcRoutes(m,n-1)

#for i in range(1,20):
#    print(str(i) + " -> " + str(calcRoutes(i,i)))

print(__file__ + ": answer: " + str(calcRoutes(20,20)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
