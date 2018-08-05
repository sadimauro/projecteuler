#!/usr/bin/python3

import time
tStart = time.time()

import stevepe as s

def getTri(i):
    return i*(i+1)/2

i = 286
foundTri = 0
while True:
    tri = getTri(i)
    if s.isPentagonal(tri) and s.isHexagonal(tri):
        foundTri = int(tri)
        break
    i += 1

print(__file__ + ": answer: " + str(foundTri))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
