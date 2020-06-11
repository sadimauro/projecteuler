#!/usr/bin/python3

from math import floor, sqrt

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

# continued fraction representation
class CFR:
    def __init__(self, n):
        self.n = n
        self.a0 = None
        self.ais = []
        self.find_a_vals()

    def find_a_vals(self):
        self.a0 = floor(sqrt(self.n))

        # addend to ai is (sqrt(self.n) + na) / d
        # n = 23; 
        #    a0 = 4; na = first_na = -4; d = first d = 1
        #    a1 = 1; na = -3; d = 7
        na = (-1) * self.a0
        d = 1
        first_na = na
        first_d = d
        while True:
            logging.debug(f"start of while; na = {na}; d = {d}")

            new_a = 0
            d = (self.n - (na * na)) // d
            na = (-1) * na
            logging.debug(f"mid-iteration, before reducing: na = {na}; d = {d}")

            while sqrt(self.n) + na > d:
                na = na - d
                new_a += 1
            
            logging.debug(f"while iteration complete; na = {na}; d = {d}; new_a = {new_a}")

            self.ais.append(new_a)
            
            if na == first_na and d == first_d:
                logging.debug(f"found recursion; exiting while")
                return

    def get_period(self):
        return len(self.ais)

    def __str__(self):
        ret = ''
        ret += f"sqrt({self.n}) = [{self.a0}; {self.ais}], period={self.get_period()}"
        return ret

count = 0
for i in range(1, 10000+1):
    logging.debug(f"calculating {i}")
    sqrt_i = sqrt(i)
    if floor(sqrt_i) == sqrt_i:
        logging.debug("not an itrrational sqrt; skipping")
        continue
    c = CFR(i)
    if c.get_period() % 2 == 1:
        count += 1

print("{}: answer: {!s}".format(__file__, count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
