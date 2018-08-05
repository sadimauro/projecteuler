#!/usr/bin/python3

import time
tStart = time.time()

import stevepe

def concatProd(intIn, n):
    """Take the number 192 and multiply it by each of 1, 2, and 3:
      192 × 1 = 192
      192 × 2 = 384
      192 × 3 = 576
    By concatenating each product we get 192384576. We will call 
    192384576 the concatenated product of 192 and (1,2,3).  In this
    case, IntIn = 192 and n = 3.
    """

    if n <= 0:
        return 0

    retStr = ""
    for thisN in range(1,n+1):
        retStr += str(intIn*thisN)

    return int(retStr)

largestOneToNinePan = 0

for i in range(1,100000):
    for j in range(2,10):
        thisProd = concatProd(i,j)
        if len(str(thisProd)) == 9:
            if stevepe.isIntPandigital(thisProd):
                print("found 1-9 pandigital! i = " + str(i) + "; j = " + str(j) + "; prod = " + str(thisProd))
                if thisProd > largestOneToNinePan:
                    largestOneToNinePan = thisProd

print(__file__ + ": answer: " + str(largestOneToNinePan))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
