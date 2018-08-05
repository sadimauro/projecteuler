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
        
import time
tStart = time.time()

# code goes here
#logging.debug("This is a debug message.")
#logging.info("This is an info message.")
#logging.warn("This is a warning message.")

print("{}: answer: {!s}".format(__file__, 999))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
