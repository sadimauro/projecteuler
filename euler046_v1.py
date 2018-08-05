#!/usr/bin/python3

import time
tStart = time.time()

import stevepe as s

def nextOddComposite(n):
    """
    Return the composite number greater than n.
    n is expected to be odd.
    """
    i = n+2
    while True:
        if s.isComposite(i):
            return i
        else:
            i += 2

growingPrimeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
growingSquareList = [1, 4, 9, 16, 25]
thisOddComp = 33
smallestOddComp = 999999999999999
smallestOddCompFound = False

thisOddComp = nextOddComposite(thisOddComp)
while not smallestOddCompFound:
    # grow Lists based on new val of thisOddComp
    n = s.getNextOddPrime(growingPrimeList[-1])
    while n < thisOddComp:
        growingPrimeList.append(n)
        n = s.getNextOddPrime(n)

    n = s.getNextSquare(growingSquareList[-1])
    while n < thisOddComp:
        growingSquareList.append(n)
        n = s.getNextSquare(n)

    # test; if found, break
    foundSum = False
    #print("prime and square lists: {!s}, {!s}".format(growingPrimeList, growingSquareList))
    for prime in growingPrimeList:
        for square in growingSquareList:
            if thisOddComp == prime + (2*square):
                foundSum = True
                
    if not foundSum:
        smallestOddComp = thisOddComp
        smallestOddCompFound = True

    # get next odd composite for testing
    thisOddComp = nextOddComposite(thisOddComp)

print("{}: answer: {!s}".format(__file__, smallestOddComp))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
