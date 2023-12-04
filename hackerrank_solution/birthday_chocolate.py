#!/bin/python3

import sys

def getWays(squares, d, m, n):
    count = 0
# how many time the loop run
    t = n-m+1
# loop to check the cake piece
    for i in range(t):
        su = 0
        n = i + m
        # loop to sum the next m numbers
        for j in range(i, n):
            su += squares[j]
        if su == d:
            count += 1

    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m, n)
print(result)
