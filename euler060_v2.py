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

lowest_sum = 999999
good_tups = []

next_prime = 1
while next_prime < 99999:
    logging.debug(f"good_tups currently {good_tups}")

    next_prime = getNextOddPrime(next_prime)
    logging.info(f"next_prime = {next_prime}")
    insert_idx = len(good_tups)

    logging.debug(f"appending next_prime {next_prime} to good_tups")
    good_tups.append((next_prime,))

    for i in range(insert_idx):
        # case 1: good_tups[i] is len 1
        if len(good_tups[i]) == 1:
            if (
                    isPrime(int(str(good_tups[i][0]) + str(next_prime)))
                    and isPrime(int(str(next_prime) + str(good_tups[i][0])))
                    ):
                new_tup = (good_tups[i][0], next_prime)
                logging.debug(f"appending case 1 new tup {new_tup}")
                good_tups.append(new_tup)

        # case 2: good tups[i] is len >1
        elif 1 < len(good_tups[i]) < 5:
            logging.debug(f"in case 2; {good_tups[i]} + {next_prime}")
            is_good = True
            for n in good_tups[i]:
                if (n, next_prime) not in good_tups[insert_idx:]:
                    is_good = False
                    break
            if is_good == True:
                new_tup = good_tups[i] + ((next_prime,))
                logging.debug(f"appending case 2 new tup {new_tup}")
                good_tups.append(new_tup)

                if len(new_tup) == 5:
                    this_sum = sum(new_tup)
                    logging.info(f"found length-5 tuple of primes: {new_tup}; sum = {this_sum}")
                    if this_sum < lowest_sum:
                        logging.info(f"setting {this_sum} to lowest_sum")
                    
print("{}: answer: {!s}".format(__file__, lowest_sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
