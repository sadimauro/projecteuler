#!/usr/bin/python3

import time
tStart = time.time()

def collatzLen(n):
    """ Input: n, Output: list of the collatz sequence starting at n"""
    newListLen = 1

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        newListLen += 1

    return newListLen

longestChainLen = 0
longestChainNum = 0
for n in range(1,int(1e6)):
    thisCLen = collatzLen(n)
    if thisCLen > longestChainLen:
        longestChainLen = thisCLen
        longestChainNum = n

print(__file__ + ": answer: " + str(longestChainNum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
