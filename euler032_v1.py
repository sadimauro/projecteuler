#!/usr/bin/python3

import time
tStart = time.time()

import itertools

def tupleToNum(tupIn):
    res = 0
    for i in range(len(tupIn)):
        res *= 10
        res += tupIn[i]
    return res

ALLSET = {1, 2, 3, 4, 5, 6, 7, 8, 9}
ALLSETLEN = 9

foundProds = set()

for mcand1Size in range(1,4+1):
    mcand1Tups = itertools.permutations(ALLSET, mcand1Size)
    for mcand1Tup in mcand1Tups:

        for mcand2Size in range(1,(ALLSETLEN-mcand1Size-4)+1):
            mcand2Tups = itertools.permutations(ALLSET-set(mcand1Tup),mcand2Size)
            for mcand2Tup in mcand2Tups:
        
                prodTups = itertools.permutations(ALLSET-set(mcand1Tup)-set(mcand2Tup))
                for prodTup in prodTups:

                    if tupleToNum(mcand1Tup) * tupleToNum(mcand2Tup) == tupleToNum(prodTup):
                        foundProds.add(tupleToNum(prodTup))

prodSum = 0
for x in foundProds:
    prodSum += x

print(__file__ + ": answer: " + str(prodSum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
