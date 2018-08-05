#!/usr/bin/python3

import time
tStart = time.time()

def nameVal(nameIn):
    sum = 0
    for i in range(len(nameIn)):
        sum += ord(nameIn[i]) - 64
    return sum

import csv
f = open("names.txt", 'r')
csvreader = csv.reader(f)
for row in csvreader:
    nameList = row

nameList.sort()

sum = 0
i = 0
for item in nameList:
    sum += (i+1) * (nameVal(item))
    i += 1

print(__file__ + ": answer: " + str(sum))
print("Run time: " + '{:.20f}'.format(time.time() - tStart) + " sec")
