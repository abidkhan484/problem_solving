#!/bin/python3

import sys

def getMagicNumber(s, k, b, m):
    # this loop is to remove the first consecutive zeros
    l = len(s)
    for i in range(l):
        if s[i] != '0':
            s[i:]
    l = len(s)
    result = 0

    # loop to get the result
    while l >= k:
        j = l-1
        i = 0; summation = 0
        temp = j-k

        # loop to get the converstion
        while j > temp:
            summation += (b**i) * int(s[j])
            i += 1
            j -= 1

        summation = summation % m
        result += summation

        l -= 1

    return result


s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
