#!/usr/bin/python3

import time
tStart = time.time()

numsInWordsDict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
        }

def getNumString(n):
    if n == 1000:
        return "one thousand"
    
    strOut = ""
    
    hundredsPart = n // 100
    if hundredsPart > 0:
        strOut += numsInWordsDict[hundredsPart] + " hundred "
        if n % 100 > 0:
            strOut += "and "

    tensAndOnesPart = n % 100
    if tensAndOnesPart > 0 and tensAndOnesPart <= 20:
        strOut += numsInWordsDict[tensAndOnesPart]
        return strOut

    tensPart = ((n % 100) // 10) * 10
    if tensPart > 0:
        strOut += numsInWordsDict[tensPart]
    onesPart = n % 10

    if onesPart > 0:
        if tensPart > 0:
            strOut += "-"
        strOut += numsInWordsDict[onesPart]
    
    return strOut

def getStrLen(strIn):
    strIn = strIn.replace(" ","")
    strIn = strIn.replace("-","")
    return len(strIn)

totalLettersUsed = 0
for i in range(1,1001):
    totalLettersUsed += getStrLen(getNumString(i))

print(__file__ + ": answer: " + str(totalLettersUsed))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
