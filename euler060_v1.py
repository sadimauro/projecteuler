#!/usr/bin/python3

from stevepe import getNextOddPrime, isPrime
from itertools import combinations

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

lowest_sum = None
primes_list_strs = []

# ignore 2, since 2 cat'ed at the end of any number will be composite.
next_prime = 1
for i in range(4):
    next_prime = getNextOddPrime(next_prime)
    primes_list_strs.append(str(next_prime))

next_prime = getNextOddPrime(next_prime)
while next_prime < 100000:
    logging.debug(f"next prime = {next_prime}")
    primes_list_strs.append(str(next_prime))
    next_prime = getNextOddPrime(next_prime)
    for combo_seed in combinations(primes_list_strs, 4):
        combo_five = combo_seed + (str(next_prime),)
        found_it = True
        for pair in combinations(combo_five, 2):
            if not isPrime(int(pair[0] + pair[1])):
                found_it = False
                break
            if not isPrime(int(pair[1] + pair[0])):
                found_it = False
                break
        if found_it:
            logging.debug(f"found candidate; combo_five = {combo_five}")
            combo_sum = 0
            for item in combo_five:
                combo_sum += int(item)
            if combo_sum < lowest_sum or lowest_sum == None:
                logging.debug(f"found low sum candidate = {combo_sum}")
                lowest_sum = combo_sum

print("{}: answer: {!s}".format(__file__, lowest_sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
