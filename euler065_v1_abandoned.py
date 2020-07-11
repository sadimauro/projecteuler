#!/usr/bin/python3

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

def find_ni(idx):
    logging.debug(f"calling find_ni with idx = {idx}")
    if idx == 0:
        return 2
    elif idx == 1:
        return 3
    else:
        return (find_ai(idx) * find_ni(idx-1)) + find_ni(idx-2)

n_100 = find_ni(100)

print("{}: answer: {!s}".format(__file__, getDigitalSum(n_100)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
