#!/usr/bin/python3

from stevepe import isIntPalindrome, getIntReverse

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

def is_lychrel(n, iters):
    logging.debug(f"calling is_lychrel with n = {n}, iters = {iters}")
    if iters >= 50:
        return True
    new_sum = n + getIntReverse(n)
    if isIntPalindrome(new_sum):
        logging.debug(f"{new_sum} is a palindrome (?)")
        return False
    return is_lychrel(new_sum, iters+1)

count = 0
for i in range(1,10000):
    logging.debug(f"*** calling is_lychrel with n = {i}")
    if is_lychrel(i, 0):
        count += 1

print("{}: answer: {!s}".format(__file__, count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
