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

STARTING_PRIME = 11#56003
STARTING_PRIME_IDX = 5#5683
FAMILY_LEN = 8
MAX_TO_TRY = 1000000

import stevepe
primes = stevepe.getPrimesBelowBySieve(MAX_TO_TRY)

import itertools
import sys

# start at starting prime
thisPrime = STARTING_PRIME
thisPrimeAsList = list(str(thisPrime))
thisPrimeIdx = STARTING_PRIME_IDX
while thisPrime < MAX_TO_TRY and thisPrimeIdx < len(primes):
    if thisPrimeIdx % 1000 == 0:
        logging.info("Testing prime {!s} at index {!s}...".format(thisPrime, thisPrimeIdx))
    
    # swap out 1...len(thisPrime)-1 combos
    for comboLen in range(1,len(thisPrimeAsList)):
        logging.debug("  combo len = {!s}".format(comboLen))
        
        # try each of the different ways to substitute out
        # comboLen numbers
        for thisComboIndices in itertools.combinations(range(len(thisPrimeAsList)), comboLen):
            logging.debug("  combo indices = {!s}".format(thisComboIndices)) 
            resultingPrimesList = []
            
            # swap in each of the 10 integers
            for i in range(10):
                # don't want to swap 0 in the first position.
                if i == 0 and 0 in thisComboIndices:
                    continue
                
                thisPrimeSwapAsList = thisPrimeAsList.copy()
                for idx in thisComboIndices:
                    thisPrimeSwapAsList[idx] = str(i)
                
                # turn list back into an int
                thisPrimeSwapAsStr = ''.join(str(c) for c in thisPrimeSwapAsList)
                logging.debug("    this swap = {}".format(thisPrimeSwapAsStr))
                
                if stevepe.isPrime(int(thisPrimeSwapAsStr)):
                    resultingPrimesList.append(int(thisPrimeSwapAsStr))
            
            logging.debug("    resulting primes count = {!s}".format(len(resultingPrimesList)))
            if len(resultingPrimesList) == FAMILY_LEN:
                # YAY!  We found what we're looking for.
                print("\n\n{}: answer: {!s}".format(__file__, min(resultingPrimesList)))
                print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
                sys.exit()

    # iterate to next prime
    thisPrimeIdx += 1
    if thisPrimeIdx < len(primes):
        thisPrime = primes[thisPrimeIdx]
        thisPrimeAsList = list(str(thisPrime))
