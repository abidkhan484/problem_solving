#!/bin/python3

import sys
import string

s = input().strip()
letters = string.ascii_lowercase

s = s.lower()
for i in s:
    l = len(letters)-1
    while l >= 0:
        if i==letters[l]:
            letters = letters[:l]+letters[l+1:]
            break
        l -= 1

if letters:
    print("not pangram")
else:
    print("pangram")


'''
another solution
-----------------------------
if len(set(input().lower().strip())) != 27:
    print("not pangram")
else:
    print("pangram")

'''
