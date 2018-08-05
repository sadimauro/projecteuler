#!/usr/bin/python3

import time
tStart = time.time()

def isTrip(a,b,c):
    return pow(a,2) + pow(b,2) == pow(c,2)

for a in range(1,1000):
    for b in range(a,1000):
        if isTrip(a, b, 1000-b-a):
            ans = a*b*(1000-b-a)
            break    

print(__file__ + ": answer: " + str(ans))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
