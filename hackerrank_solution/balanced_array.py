#!/bin/python3

import sys

def solve(a):
    left_sum = 0
    right_sum = 0
    m =len(a)
    n = m // 2
    for i in range(n):
        left_sum += a[i]
        right_sum += a[m-i-1]
            
    if left_sum > right_sum:
        return left_sum-right_sum
    elif right_sum > left_sum:
        return right_sum-left_sum
    else:
        return 0

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)
