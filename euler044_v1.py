#!/usr/bin/python3

import time
tStart = time.time()

NUM_PENTAGS = 5000
pentags = list()

# First, generate a big list of pentagonal numbers
for i in range(1,NUM_PENTAGS+1):
    pentags.append(i * (3*i - 1) // 2)

overallMin = 9999999999

# grab pairs of pentagonal numbers...
for j in range(0, NUM_PENTAGS):
    for k in range(j+1, NUM_PENTAGS):
        if (pentags[j] + pentags[k]) in pentags:
            diff = pentags[k] - pentags[j]
            if diff in pentags:
                if diff < overallMin:
                    overallMin = diff

print(__file__ + ": answer: " + str(overallMin))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
