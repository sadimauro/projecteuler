#!/usr/bin/python3

import time
tStart = time.time()

def daysInMonth(thisMonth,thisYear):
    if thisMonth in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thisMonth in [9, 4, 6, 11]:
        return 30
    else:
        # February = 2
        if thisYear % 400 == 0:
            return 29
        elif thisYear % 100 == 0:
            return 28
        elif thisYear % 4 == 0:
            return 29
        else:
            return 28

countFirstSundays = 0

# 1 jan 1901 = Tuesday = 2
thisDOW = 2

for year in range(1901,2001):
    for month in range(1,13):
        thisDOW = (thisDOW + daysInMonth(month,year)) % 7
        if thisDOW == 0:
            countFirstSundays += 1

print(__file__ + ": answer: " + str(countFirstSundays))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
