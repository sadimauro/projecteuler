#!/usr/bin/python3

import time
tStart = time.time()

i = 1
s = ""
while len(s) < 1000000:
    s += str(i)
    i += 1

print(__file__ + ": answer: " + str(\
        int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])\
        ))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
