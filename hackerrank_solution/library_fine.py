#!/bin/python3

import sys
'''
def test(d1,m1,y1,d2,m2,y2):
    if y1<=y2:
        return 0
        if m1<=m2:
            return 0
            if d1<=d2:
                return 0
            else:
                return (d1-d2)*15
        else:
            return (m1-m2)*500
    else:
        return (y1-y2)*10000
'''
d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0
if d1>d2:
    temp = d1-d2
    fine = temp*15
if m1>m2:
    temp = m1-m2
    fine = temp*500
if y1>y2:
    temp = y1-y2
    fine = temp*10000
if y1<y2:
    fine = 0
if y1<=y2 and m1<m2:
    fine = 0

#fine = test(d1,m1,y1,d2,m2,y2)
print(fine)
