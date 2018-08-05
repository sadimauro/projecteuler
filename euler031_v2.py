#!/usr/bin/python3

import time
tStart = time.time()

# coins = 200, 100, 50, 20, 10, 5, 2, 1
COINS = [200, 100, 50, 20, 10, 5, 2, 1]
GOAL = 200

def mec(balance, coinToTryIdx):
    global count

    #print("count = " + str(count) + "; bal = " + str(balance) + "; coin to try = " + str(COINS[coinToTryIdx]))

    # case: balance == 0
    if balance == 0:
        count += 1
        return

    # case: error
    if coinToTryIdx >= len(COINS) or coinToTryIdx < 0:
        print("Error", sys.stderr)
        exit()
    
    # case: coin == 1
    if coinToTryIdx == len(COINS) - 1:
        count += 1
        return

    nCoinsInBalance = balance // COINS[coinToTryIdx]
    for i in range(-1,nCoinsInBalance):
        mec(balance-(COINS[coinToTryIdx]*(i+1)), coinToTryIdx+1)

count = 0
mec(GOAL, 0)

print(__file__ + ": answer: " + str(count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
