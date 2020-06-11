#!/usr/bin/python3

from math import ceil

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

count = 0
for n in range(1,50):
    good_bases = []
    for b in range(1,50):
        if len(str(pow(b, n))) == n:
            good_bases.append(b)
            count += 1
    logging.debug(f"{n:2d} good bases: {good_bases}")

print("{}: answer: {!s}".format(__file__, count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
