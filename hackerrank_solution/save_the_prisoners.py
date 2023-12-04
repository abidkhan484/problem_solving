#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    s -= 1
    s += m
    if s>=n:
        s = s%n
        if s == 0:
            s = n
    return s

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
