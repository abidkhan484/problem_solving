#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
count = 0
maxim = -1
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

    
i = 0
while i < n-1:

    # this loop run for check ith item after the ith item of topic
    k = i+1
    while k < n:

        # this loop run for, if the item of two sequencial topic
        j = 0; tmp = 0
        while j < m:
            # this logic checks if two consecutive lists item are same or not
            if (topic[i][j]=='1') or (topic[k][j]=='1'):                
                tmp += 1
            j += 1

        # this logic test if the maximum value are same or greater
        if tmp > maxim:
            maxim = tmp
            count = 1

        elif tmp==maxim:
            count +=1

        k += 1

    i += 1


print(maxim, count, end='\n')
