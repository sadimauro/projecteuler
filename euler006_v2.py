#!/usr/bin/python3

import time
tStart = time.time()

sum1 = 0
sum2 = 0

sum1 = sum([i**2 for i in range(1,101)])
sum2 = sum([i for i in range(1,101)]) ** 2

print("Answer: " + str(sum2 - sum1))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
