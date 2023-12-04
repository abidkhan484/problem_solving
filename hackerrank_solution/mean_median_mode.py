#!/bin/python3

import sys

# this function return the mean of the list
def mean(li):
    total = sum(li)
    l = len(li)
    return total/l

# this function return the median of the list
def median(li):
    l = len(li)
    li.sort()
    #if you don't understand this logic. then check the role of median
    if (l//2) != (l/2):
        return li[l//2]
    else:
        total = li[l//2] + li[(l//2)-1]
        return total/2

# return the mode of the list
def mode(li):
    l = len(li)
    li.sort()

    # temp list is used to append the res variable, (a number occerence time)
    # res - is used for check on the li list, how many time a number occerence
    temp = []; res = 1
    # num list is used which number on the li list is occered 'res' times
    # maxim is used for which number in temp list is maximum
    num = []; maxim = -1

    # loop to find the number which occered how many time and its position
    # num list is to temp list as its occerence time
    for i in range(l-1):
        if li[i] != li[i+1]:
            num.append(li[i])
            temp.append(res)
            if maxim < res:
                maxim = res
            res = 1
        else:
            res += 1

    # this operation is used for the last number
    num.append(li[i+1])
    temp.append(res)

    # if two or more number occered maximum time, then the loop returns the
    # lowest number
    l = len(temp)
    for i in range(l):
        if maxim == temp[i]:
            break
    
    return num[i]

n = int(input().strip())
li = list(map(int, input().split()))
print("average of the list: %.1f" %mean(li))
print("median of the list is: %.1f" %median(li))
print("mode of the list is: %.1f"%mode(li))
