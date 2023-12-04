#!/bin/usr/env python3

import sys
import math

n = int(input().strip())

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)

    temp_a = math.floor(math.sqrt(a))

    temp_b = math.floor(math.sqrt(b))
    
    if temp_a != temp_b:
        print(temp_b-temp_a, _+1)
    else:
        if a != b:
            print(0)
        else:
            print(1)
