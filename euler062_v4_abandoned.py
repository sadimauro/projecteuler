#!/usr/bin/python3

"""
v4 - even smarter storage/search of the cubes
"""

from stevepe import getIntPermutationsDeduped

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

def store_cube(d, cube, is_checked):
    high = cube // 1000
    low = cube % 1000
    if high not in d:
        d[high] = {}
    if low not in d[high]:
        d[high][low] = {}
    d[high][low] = is_checked
    return d

def mark_cube_checked(d, cube):
    high = cube // 1000
    low = cube % 1000
    d[high][low] = True
    return

def n_in_d(d, n):
    high = n // 1000
    low = n % 1000
    if high not in d:
        return False
    return low in d[high]

def check_n_in_d(d, n):
    """
    if n is in d, return True.
    If cube, also mark it checked.
    """
    if n_in_d(d, n):
        mark_cube_checked(d, n)
        return True
    else:
        return False

def is_n_in_d_and_checked(d, n):
    high = n // 1000
    low = n % 1000
    if high not in d:
        return False
    if low not in d[high]:
        return False
    return d[high][low]


seed = 0
cubes = {}
max_cube = 0
max_cube_seed = 0
while True:
    seed += 1

    cube = pow(seed, 3)
    logging.debug(f"seed = {seed}; cube = {cube}") 

    # if cube is already in d and checked, we've already explored the "cycle" within which cube
    # is a member.  So don't waste time testing it.
    if is_n_in_d_and_checked(cubes, cube):
        logging.debug(f"cube already in dict and checked; skipping")
        continue

    cubes_from_perms = 0

    deduped_perms = getIntPermutationsDeduped(cube)
    for perm in deduped_perms:
        #logging.debug(f"testing perm {perm}")
        if perm > max_cube:
            while perm > max_cube:
                max_cube_seed += 1
                max_cube = pow(max_cube_seed, 3)
                #logging.debug(f"extending cubes by appending {max_cube}")
                store_cube(cubes, max_cube, False)
            logging.debug(f"added cubes to d; d now has {len(cubes.keys())} keys")

        if check_n_in_d(cubes, perm):
            logging.debug(f"{perm} is a cube")
            cubes_from_perms += 1

    logging.debug(f"found {cubes_from_perms} cubes")
    if cubes_from_perms == 5:
        print("{}: answer: {!s}".format(__file__, cube))
        print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")


