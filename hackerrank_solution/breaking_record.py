#!/bin/python3

import sys


def getRecord(s):
    # Complete this function
    l = len(s)
    lar = s[0]; less=s[0]
    c=0; d=0
    for i in range(1, l):
        if(s[i] < less):
            less = s[i]
            d += 1
        if(s[i] > lar):
            lar = s[i]
            c += 1
    return c,d

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
