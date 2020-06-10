#!/usr/bin/python3

"""
v3 - smarter storage/search of the cubes
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

def store_cube(d, cube):
    high = cube // 10000
    low = cube % 10000
    if high not in d:
        d[high] = []
    d[high].append(low)
    return d

def cube_in_d(d, cube):
    high = cube // 10000
    low = cube % 10000
    if high not in d:
        return False
    return low in d[high]

seed = 345
cubes = {}
for i in range(seed+1):
    cube = pow(seed, 3)
    store_cube(cubes, cube)

max_cube = cube
max_cube_seed = seed

seed += 1

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
                store_cube(cubes, max_cube)
        if cube_in_d(cubes, perm):
            logging.debug(f"{perm} is a cube")
            cubes_from_perms += 1

    logging.debug(f"found {cubes_from_perms} cubes")
    if cubes_from_perms == 5:
        print("{}: answer: {!s}".format(__file__, cube))
        print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")

    seed += 1


