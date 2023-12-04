#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

c.sort()

maxim = -1; j = 0
for i in range(n):
    dis = min(abs(i-c[j]), abs(i-c[j+1]))
