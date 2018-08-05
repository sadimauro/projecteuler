#!/usr/bin/python3

import time
tStart = time.time()

def collatz(n):
    """ Input: n, Output: list of the collatz sequence starting at n"""
    newList = []
    newList.append(n)

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        newList.append(n)
    return newList

longestChainLen = 0
longestChainNum = 0
for n in range(1,int(1e6)):
    if len(collatz(n)) > longestChainLen:
        longestChainLen = len(collatz(n))
        longestChainNum = n

print(__file__ + ": answer: " + str(longestChainNum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
