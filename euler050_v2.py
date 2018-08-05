#!/usr/bin/python3

import time
tStart = time.time()

MAX_TO_TRY = 1000000

import stevepe

primesTup = tuple(stevepe.getPrimesBelow(MAX_TO_TRY))

longestTerms = 0
longestTermsPrime = 0

for pttIdx in range(len(primesTup)):
    # start at the start of primesTup; add primes until either
    # the sum is == prime or > prime.
    #
    # Then repeat starting at the next prime, and do this all
    # again until start > prime.
    lb = 0
    while primesTup[lb] < primesTup[pttIdx]:
        i = lb + longestTerms
        thisSum = sum(primesTup[lb:i])
        while primesTup[i] < primesTup[pttIdx] and i < len(primesTup):
            thisSum += primesTup[i]
            if thisSum == primesTup[pttIdx]:
                if (i-lb+1) > longestTerms:
                    longestTerms = i-lb+1
                    longestTermsPrime = thisSum
                    print("found prime sum ({}); lb = {}; i = {}, seq len = {}".format(str(thisSum), str(lb), str(i), str(longestTerms)))
            i += 1
        lb += 1

print("{}: answer: {!s}".format(__file__, longestTermsPrime))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
