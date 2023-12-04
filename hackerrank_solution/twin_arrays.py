#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    m = len(ar1)
    n = len(ar2)

    mini = 100001
    for i in range(m):
        for j in range(n):
            if (i != j):
                if ((ar1[i]+ar2[j]) < mini):
                    mini = ar1[i] + ar2[j]

    return mini

    
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
