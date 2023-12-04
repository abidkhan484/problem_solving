#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

height.sort()
if height[-1] <= k:
    print(0)
else:
    print(height[-1] - k)
