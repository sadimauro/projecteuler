#!/usr/bin/python3

import time
tStart = time.time()


import stevepe

MAX_PRIME = 1000000
p = tuple(stevepe.getPrimesBelow(MAX_PRIME))

# strategy:  define max and min window size;
# for each window size i, slide a window across the set of primes.
# Once we find a sequence of len i, quit, because we're looking
# for a long one.
WINDOW_LEN_MAX = 50000
WINDOW_LEN_MIN = 1

for window_len in range(WINDOW_LEN_MAX, WINDOW_LEN_MIN-1, -1):
    print("window len = {!s}".format(window_len))
    
    i = 0
    thisSum = sum(p[i:(i+window_len)])
    #print("calculating sum over indices {!s}...{!s} inclusive".format(i, i+window_len-1))
    while (i+window_len) < len(p) and thisSum < MAX_PRIME:

        if stevepe.isPrime(thisSum):
            # hooray!  Found a long prime sum.  Print and exit.
            print("{}: answer: {!s} ({!s} [{!s}] + ... + {!s} [{!s}])".format(__file__, thisSum, p[i], i, p[i+window_len-1], i+window_len-1))
            print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
            exit()

        # slide window
        if (i+window_len) < len(p):
            #print("calculating sum over {!s} ... {!s} inclusive".format(i+1, i+window_len))
            thisSum = thisSum - p[i] + p[i+window_len]
        i += 1
