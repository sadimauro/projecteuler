#!/usr/bin/python3

import time
tStart = time.time()

sum1 = 0
sum2 = 0

for i in range(1,101):
    sum1 += pow(i, 2)
    sum2 += i
sum2 = pow(sum2, 2)

print("Answer: " + str(sum2 - sum1))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
