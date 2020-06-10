#!/usr/bin/python3

"""
v2 - precalculate some cubes.
"""

from stevepe import getIntPermutations

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
cubes = []
for i in range(seed+1):
    cubes.append(pow(seed, 3))
seed += 1

max_cube = 0
max_cube_seed = 0

while True:
    cube = seed*seed*seed
    logging.debug(f"seed = {seed}; cube = {cube}") 

    cubes_from_perms = 0

    deduped_perms = getIntPermutations(cube)
    for perm in deduped_perms:
        #logging.debug(f"testing perm {perm}")
        if perm > max_cube:
            while perm > max_cube:
                max_cube_seed += 1
                max_cube = pow(max_cube_seed, 3)
                #logging.debug(f"extending cubes by appending {max_cube}")
                cubes.append(max_cube)
        if perm in cubes:
            logging.debug(f"{perm} is a cube")
            cubes_from_perms += 1

    logging.debug(f"found {cubes_from_perms} cubes")
    if cubes_from_perms == 5:
        print("{}: answer: {!s}".format(__file__, cube))
        print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")

    max_cube_lastiter = cubes[-1]
    seed += 1


