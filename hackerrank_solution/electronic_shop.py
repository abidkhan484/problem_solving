#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    comb=list(i+j for i in keyboards for j in drives)
    try:
        return s - min(list(s-i for i in comb if i<=s))
    except:
        return -1
                

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
