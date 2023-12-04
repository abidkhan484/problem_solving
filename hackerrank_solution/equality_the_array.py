#!/bin/python3

import sys

n = int(input().strip())
arr = [int(temp) for temp in input().split()]

arr.sort()
maxim, c = -1, 1

for i in range(1, n):
    if arr[i]==arr[i-1]:
        c += 1

    else:
        if c > maxim:
            maxim = c
        c = 1

if c > maxim:
    maxim = c
print(n - maxim)
