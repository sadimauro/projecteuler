#!/usr/bin/python3

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

def find_lowest_form(intin):
    l = list(str(intin))
    l.sort()
    return ''.join(l)

import time
tStart = time.time()

# lowest_form_str -> (least cube, count)
cubes = {}

n = 0
while True:
    n += 1

    cube = pow(n, 3)
    logging.info(f"testing {n} -> {cube}")

    cube_lf_str = find_lowest_form(cube)
    logging.debug(f"lowest form = {cube_lf_str}")
    if cube_lf_str in cubes:
        cubes[cube_lf_str][1] += 1
        logging.debug(f"found perm of existing cube; count now {cubes[cube_lf_str][1]}")
        if cubes[cube_lf_str][1] == 5:
            print("{}: answer: {!s}".format(__file__, cubes[cube_lf_str][0]))
            print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
            exit(1)
    else:
        cubes[cube_lf_str] = [cube, 1]
