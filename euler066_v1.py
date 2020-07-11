#!/usr/bin/python3

from stevepe import isSquare
import math

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

largest_x = 0
largest_x_d = 0

def is_square(n):
    return isSquare(n)

# precompute y
Y2_MAX_COUNT = 2**20
Y2 = [y**2 for y in range(1,Y2_MAX_COUNT+1)]

# x**2 - D*y**2 = 1 -->

def find_min_x(d):
    for idx in range(Y2_MAX_COUNT):
        logging.debug(f"in find_min_x: d = {d}, testing y = {Y2[idx]}")
        inner = 1 + (d * Y2[idx])
        logging.debug(f"inner = {inner}")
        #if inner in Y2:
        if is_square(inner):
            logging.debug(f"{inner} is square")
            return int(math.sqrt(inner))
    raise Exception("Y_MAX too small")

for d in range(1, 1000+1):
    logging.info(f"testing {d}")
    if is_square(d):
        logging.debug(f"{d} is a square; skipping")
        continue
    min_x = find_min_x(d)
    logging.debug(f"min x = {min_x}")
    if min_x > largest_x:
        largest_x = min_x
        largest_x_d = d

print("{}: answer: {!s}".format(__file__, largest_x_d))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
