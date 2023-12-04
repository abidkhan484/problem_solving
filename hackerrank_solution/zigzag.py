#!/bin/python3

import sys

def minimumDeletions(a):
    # Complete this function

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Return the minimum number of elements to delete to make the array zigzag
result = minimumDeletions(a)
print(result)
