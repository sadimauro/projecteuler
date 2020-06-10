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

ds_max = 0
for a in range(1,100):
    for b in range(1,100):
        ds = getDigitalSum(a**b)
        ds_max = ds if ds > ds_max else ds_max


print("{}: answer: {!s}".format(__file__, ds_max))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
