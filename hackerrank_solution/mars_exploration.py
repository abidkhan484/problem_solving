#!/bin/python3

import sys

s = input().strip()

count = 0
s = list(s)
l = len(s); j = 0

msg = list('SOS')
for i in range(l):
    if s[i] != msg[j]:
        count += 1
    j += 1
    if j == 3:
        j = j%3

print(count)


"""
another solution:

print(len([1 for x,y in zip(input(),'SOS'*33) if x!=y]))
"""
