#!/usr/bin/python3

import time
tStart = time.time()

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
                            
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

ans = 1
for i in range(1,21):
    ans = lcm(i, ans)

print("Answer: " + str(ans))
print("Run time: " + str((time.time() - tStart)) + " sec")
