#!/usr/bin/python3

import time
tStart = time.time()

import itertools

def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(itertools.islice(iterable, n, None), default)

perms = itertools.permutations(range(10))

print(__file__ + ": answer: " + str(nth(perms, 999999)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
