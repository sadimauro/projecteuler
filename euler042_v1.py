#!/usr/bin/python3

import time
tStart = time.time()

FILENAME = "./p042_words.txt"
MAX_LETTER_VAL = 26

f = open(FILENAME, 'r')
mystr = f.readline()
mylist = mystr.split(',')
longestWord = 0
for i in range(len(mylist)):
    mylist[i] = mylist[i].strip('"')
    if len(mylist[i]) > longestWord:
        longestWord = len(mylist[i])

# generate trinagular number list that will be
# as long as we need it:  MAX_LETTER_VAL * 
# longestWord
def triNum(n):
    return (n * (n+1)) // 2
triNumSet = set()
n = 1
thisTriNum = triNum(n)
while thisTriNum <= (MAX_LETTER_VAL * longestWord):
    triNumSet.add(thisTriNum)
    n += 1
    thisTriNum = triNum(n)

# for each word, calculate the total word value
# and test if it is in the list of triangular numbers
def calcWordVal(wordIn):
    ret = 0
    for i in range(len(wordIn)):
        ret += ord(wordIn[i]) - 64
    return ret

count = 0
for word in mylist:
    if calcWordVal(word) in triNumSet:
        count += 1

print(__file__ + ": answer: " + str(count))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
