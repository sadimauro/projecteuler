#!/usr/bin/python3

import time
tStart = time.time()

import stevepe
import itertools

n = 2
firstInt = 0
primesToTry = [2]
while True:
    # get additional primes to try, between max in the primes list and n
    additionalPrimes = stevepe.getPrimesBetween(primesToTry[-1], n)
    if len(additionalPrimes) > 0:
        list2d = [primesToTry, additionalPrimes]
        primesToTry = list(itertools.chain.from_iterable(list2d))

    # find the number of prime factors
    thisPrimeFactors = list()
    i = 0
    nCopy = n
    while i < len(primesToTry) and primesToTry[i] <= nCopy:
        if nCopy % primesToTry[i] == 0:
            thisPrimeFactors.append(primesToTry[i])
            nCopy = nCopy // primesToTry[i]
        else:
            i += 1

    if len(set(thisPrimeFactors)) == 4:
        if n - firstInt == 3:
            break
        if firstInt == 0:
            firstInt = n
    else:
        firstInt = 0
    
    n += 1

print("{}: answer: {!s}".format(__file__, firstInt))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
