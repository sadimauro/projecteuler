#!/usr/bin/python3

from stevepe import isPrime

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

side_len = 1
primes_count = 0
total_count = 1
last_digit = 1

while True:
    side_len += 2
    for i in range(4):
        last_digit += (side_len-1)
        if isPrime(last_digit):
            primes_count += 1
    total_count += 4

    logging.debug(f"{primes_count} / {total_count}")

    if primes_count / total_count < .1:
        break

print("{}: answer: {!s}".format(__file__, side_len))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
