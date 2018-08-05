#!/usr/bin/python3

import time
tStart = time.time()

STR = "0123456789"

import stevepe as s
import itertools

overallSum = 0

for tup in itertools.permutations(STR):
    if s.tupleToInt(tup[1:4]) % 2 == 0 and\
            s.tupleToInt(tup[2:5]) % 3 == 0 and\
            s.tupleToInt(tup[3:6]) % 5 == 0 and\
            s.tupleToInt(tup[4:7]) % 7 == 0 and\
            s.tupleToInt(tup[5:8]) % 11 == 0 and\
            s.tupleToInt(tup[6:9]) % 13 == 0 and\
            s.tupleToInt(tup[7:10]) % 17 == 0:
                overallSum += s.tupleToInt(tup)

print(__file__ + ": answer: " + "{!s}".format(overallSum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
