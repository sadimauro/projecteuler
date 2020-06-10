#!/usr/bin/python3

""" 
v4
In this version, using a dict and masks to store the numbers, and will recursively search to find a cycle.
"""
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
    return n*(2*n-1)
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

GS = [g_3, g_4, g_5, g_6, g_7, g_8]

def searchd(d, pre, initial_pre, needed_mask, sum_so_far):
    """ 
    Recursively search dictionary d, starting at pre and needed_mask
    lsb of needed_mask corresponds to the lowest-dimension polygonal number
    """
    needed_mask_den = 0
    for i in range(6):
        needed_mask_den += (needed_mask >> i) & 1

    logging.debug(f"{(6-needed_mask_den)*' '}" + f"searchd start; pre = {pre}; needed_mask = {bin(needed_mask)}; sum_so_far = {sum_so_far}")
    if pre not in d:
        return
    suf_d = d[pre]
    for suf in suf_d.keys():
        suf_mask = suf_d[suf]
        new_mask = suf_mask & needed_mask
        for i in range(6):
            # does this idx represent a polygonal number I need?
            if (new_mask >> i) & 1 == 1:
                # yes it does!

                # clear the bit from needed_mask
                this_needed_mask = needed_mask ^ (1 << i)
                
                # add the (four-digit) number to the sum
                this_sum_so_far = sum_so_far + ((pre * 100) + suf)

                # have we found all 6 numbers?
                if this_needed_mask == 0:
                    if suf == initial_pre:
                        print("{}: answer: {!s}".format(__file__, this_sum_so_far))
                        #print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
                        exit(1)
                    else:
                        return

                # recursively search
                searchd(d, suf, initial_pre, this_needed_mask, this_sum_so_far) 

def main():
    found_sum = 0

    # build dict
    d = {}
    for i in range(6):
        for n in GS[i]():
            pre = n // 100
            suf = n % 100
            if pre not in d:
                d[pre] = {}
            if suf not in d[pre]:
                d[pre][suf] = 0x00
            d[pre][suf] |= (1 << i)

    logging.debug(f"d = {d}")

    # recursively search dict
    for pre in d:
        searchd(d, pre, pre, 0x3f, 0)


if __name__ == "__main__":
    main()
