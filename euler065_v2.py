#!/usr/bin/python3

"""
v2 -
simple recursion didn't complete.
Instead, recurse from bottom-up.
"""

from stevepe import getDigitalSum

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

def find_ai(idx):
    if idx == 0:
        return 2
    else:
        if idx % 3 == 2:
            return 2 * (idx // 3) + 2
        else:
            return 1

def find_ni(idx, ni_minus_1, ni_minus_2):
    #if idx == 0:
    #    return 2
    #elif idx == 1:
    #    return 3
    #else:
    #    return (find_ai(idx) * find_ni(idx-1)) + find_ni(idx-2)
    return (find_ai(idx) * ni_minus_1) + ni_minus_2

ni_minus_1 = 3
ni_minus_2 = 2

for idx in range(2, 100):
    n = find_ni(idx, ni_minus_1, ni_minus_2)
    logging.debug(f"iteration {idx}: calculated n = {n} from {ni_minus_1} and {ni_minus_2}")
    ni_minus_2 = ni_minus_1
    ni_minus_1 = n

print("{}: answer: {!s}".format(__file__, getDigitalSum(n)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
