#!/usr/bin/python3

import time
tStart = time.time()

DENOMS = [200, 100, 50, 20, 10, 5, 2, 1]
GOAL = 3

def makeEnglishChange(balance, comboThusFar):
    global combos
    print("mEC; balance = " + str(balance))
    if balance == 0:
        combos.append(comboThusFar)
        return
    for denom in DENOMS:
        howManyOfThisCoin = balance // denom
        if howManyOfThisCoin > 0:
            for i in range(howManyOfThisCoin):
                comboThusFar[denom] += i+1
                makeEnglishChange(balance-((i+1)*denom), comboThusFar)
combos = []
thisCombo = {}
for denom in DENOMS:
    thisCombo[denom] = 0
makeEnglishChange(GOAL, thisCombo)

print("len of combos list = " + str(len(combos)))
for combo in combos:
    print(combo)

print(__file__ + ": answer: " + str("todo"))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
