#!/usr/bin/python3

from stevepe import numberOfDigits

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="logging level; one of DEBUG, INFO, WARNING", type=str)
args = parser.parse_args()

import logging
if args.log:
    loglevel = getattr(logging, args.log.upper())
else:
    loglevel = logging.WARN
logging.basicConfig(level=loglevel)
        
import time
tStart = time.time()

def get_next(tup):
    return tup[0]+(2*tup[1]), tup[0]+tup[1]

count = 0
val = (3,2)

for i in range(999):
    val = get_next(val)
    if numberOfDigits(val[0]) > numberOfDigits(val[1]):
        count += 1

print("{}: answer: {!s}".format(__file__, count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
