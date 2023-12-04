#!/bin/python3

import sys

string = input()
s = list(string)

while s:
    le = len(s) - 2
    counter = 0
    for i in range(le):
        if (i==le):
            counter += 1

        if (s[i]==s[i+1]):
            s.remove(s[i])
            s.remove(s[i+1])
            break
    if counter > 0:
        break

s = ''.join(s)
if s:
    print(s)
else:
    print("Empty String")
