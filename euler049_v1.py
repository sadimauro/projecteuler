#!/usr/bin/python3

import time
tStart = time.time()

import stevepe

for a in range(1001, 10000, 2):
    if not stevepe.isPrime(a):
        continue
    for step in range(2, (10001-a//2)+1, 2):
        b = a + step
        c = a + step + step
        perms = stevepe.getIntPermutations(a)
        if b not in perms or c not in perms:
            continue
        if not stevepe.isPrime(b) or not stevepe.isPrime(c):
            continue
        print("{}: possible answer: {!s}, {!s}, {!s}".format(__file__, a, b, c))

print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
