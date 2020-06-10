#!/usr/bin/python3

"""
v1 - Naive approach.
"""

from itertools import permutations
from stevepe import getIntPermutationsGen

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

seed = 345
while True:
    cube = seed*seed*seed
    logging.debug(f"seed = {seed}; cube = {cube}")
    cubes_from_perms = 0
    for perm in getIntPermutationsGen(cube):
        if pow(perm, (1/3)) % 1 == 0:
            cubes_from_perms += 1
    logging.debug(f"found {cubes_from_perms} cubes")
    if cubes_from_perms == 5:
        print("{}: answer: {!s}".format(__file__, cube))
        print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")

    seed += 1


