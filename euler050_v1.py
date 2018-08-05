#!/usr/bin/python3

import time
tStart = time.time()

MAX_TO_TRY = 1000000
MAX_TERM_LEN = 20

import stevepe

primesTup = tuple(stevepe.getPrimesBelow(MAX_TO_TRY))
print("len of primesTup = {}".format(str(len(primesTup))))

longestTerms = 0
longestTermsPrime = 0

for lb in range(0,len(primesTup)):
    print("lb = {}".format(str(lb))) 
    ublimit = lb + MAX_TERM_LEN
    if ublimit > len(primesTup):
        ublimit = len(primesTup)

    for ub in range(lb,ublimit):
        thisSum = sum(primesTup[lb:ub])
        if thisSum in primesTup:
            if (ub-lb) > longestTerms:
                longestTerms = (ub-lb)
                longestTermsPrime = thisSum

print("{}: answer: {!s}".format(__file__, longestTermsPrime))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
