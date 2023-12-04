#!/bin/python3

import sys

def timeCompare(t1, t2):
    # Complete this function
    t1 = t1.split(':')
    t2 = t2.split(':')

    if (t1[1][2] > t2[1][2]):
        return 'Second'
    elif (t1[1][2] < t2[1][2]):
        return 'First'
    else:
        t1[0] = int(t1[0])
        t2[0] = int(t2[0])
        t1[1] = int(t1[1][:2])
        t2[1] = int(t2[1][:2])

        time1 = ((t1[0]%12)*60 + t1[1])
        time2 = ((t2[0]%12)*60 + t2[1])

        if time1 > time2:
            return 'Second'
        else:
            return 'First'

q = int(input().strip())
for a0 in range(q):
    t1, t2 = input().strip().split(' ')
    t1, t2 = [str(t1), str(t2)]
    result = timeCompare(t1, t2)
    print(result)
