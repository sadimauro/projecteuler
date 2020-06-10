#!/usr/bin/python3

from itertools import permutations

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

def g(f):
    n = 1
    while True:
        new = f(n)
        if 1000 <= new <= 9999 and new % 100 >= 10:
            yield new
        elif new > 9999:
            return
        n += 1

def f_3(n):
    return (n*(n+1)) // 2
def f_4(n):
    return n*n
def f_5(n):
    return (n*(3*n-1)) // 2
def f_6(n):
    return (n*(2*n-1))
def f_7(n):
    return (n*(5*n-3)) // 2
def f_8(n):
    return n*(3*n - 2)

def g_3():
    return g(f_3)
def g_4():
    return g(f_4)
def g_5():
    return g(f_5)
def g_6():
    return g(f_6)
def g_7():
    return g(f_7)
def g_8():
    return g(f_8)

def is_cyclic_tup(mytup):
    last_idx = len(mytup)-1
    for i in range(last_idx):
        if mytup[i] % 100 != mytup[i+1] // 100:
            return False
    if mytup[last_idx-1] % 100 != mytup[0] // 100:
        return False
    return True

def main():
    found_sum = 0
    for g3 in g_3():
        for g4 in g_4():
            for g5 in g_5():
                for g6 in g_6():
                    for g7 in g_7():
                        for g8 in g_8():
                            this_set = set((g3, g4, g5, g6, g7, g8))
                            if len(this_set) != 6:
                                continue
                            for perm in permutations(this_set, 6):
                                if is_cyclic_tup(perm):
                                    found_sum = sum(this_set)
                                    print("{}: answer: {!s}".format(__file__, found_sum))
                                    print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
                                    return

if __name__ == "__main__":
    main()
