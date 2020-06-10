#!/usr/bin/python3

"""
v5 - store #s as strings to avoid conversion cost;
only test perms > cube
"""

from itertools import permutations

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

N = 5

def getHighLow(n_str):
    return n_str[:-N], n_str[-N:]

def store_cube_str(d, cube_str, is_checked):
    high, low = getHighLow(cube_str)
    if high not in d:
        d[high] = {}
    if low not in d[high]:
        d[high][low] = {}
    d[high][low] = is_checked
    return d

def mark_cube_str_checked(d, cube_str):
    high, low = getHighLow(cube_str)
    d[high][low] = True
    return

def n_str_in_d(d, n_str):
    high, low = getHighLow(n_str)
    if high not in d:
        return False
    return low in d[high]

def check_n_str_in_d(d, n_str):
    """
    if n is in d, return True.
    If cube, also mark it checked.
    """
    if n_str_in_d(d, n_str):
        mark_cube_str_checked(d, n_str)
        return True
    else:
        return False

def is_n_str_in_d_and_checked(d, n_str):
    high, low = getHighLow(n_str)
    if high not in d:
        return False
    if low not in d[high]:
        return False
    return d[high][low]

def getStrPermsDeduped(strin):
    return set(''.join(perm) for perm in permutations(strin))

seed = 0
cubes = {}
max_cube = 0
max_cube_seed = 0
while True:
    seed += 1

    cube = pow(seed, 3)
    cube_as_str = str(cube)

    # if cube is already in d and checked, we've already explored the "cycle" within which cube
    # is a member.  So don't waste time testing it.
    if is_n_str_in_d_and_checked(cubes, cube_as_str):
        logging.debug(f"cube already in dict and checked; skipping")
        continue

    cubes_from_perms = 0

    deduped_str_perms = getStrPermsDeduped(cube_as_str)
    for perm_str in deduped_str_perms:
        logging.debug(f"testing perm {perm_str}")
        if int(perm_str) > max_cube:
            while int(perm_str) > max_cube:
                max_cube_seed += 1
                max_cube = pow(max_cube_seed, 3)
                #logging.debug(f"extending cubes by appending {max_cube}")
                store_cube_str(cubes, str(max_cube), False)
            logging.debug(f"added cubes to d; d now has {len(cubes.keys())} keys")

        if perm_str < cube_as_str:
            logging.debug(f"{perm_str} < {cube_as_str}; skipping")
            continue

        if check_n_str_in_d(cubes, perm_str):
            logging.debug(f"{perm_str} is a cube")
            cubes_from_perms += 1

    logging.info(f"seed = {seed}; cube = {cube}; found {cubes_from_perms} cubes")
    if cubes_from_perms == 5:
        print("{}: answer: {!s}".format(__file__, cube))
        print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")


