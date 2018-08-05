#!/usr/bin/python3

import time
tStart = time.time()

powTermsSet = set()

for a in range(2,101):
    for b in range(2,101):
       powTermsSet.add(a**b)

print(__file__ + ": answer: " + str(len(powTermsSet)))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
