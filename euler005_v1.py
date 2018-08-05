#!/usr/bin/python3

import time
tStart = time.time()

start = 2520
while True:
    isBreak = False
    for i in range(11,21):
        if start % i != 0:
            isBreak = True
            break
    if isBreak:
        start += 2
        continue
    else:
        break
                                           
print("Answer: " + str(start))
print("Run time: " + str((time.time() - tStart)) + " sec")
