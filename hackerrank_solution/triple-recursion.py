n, m, k = map(int, input().split()) # 4,3,1

def pagli(n, m, k, i=0, j=0):

    if j == n:
        i += 1
        j = 0

    if i == n:
        return

    if (i==0) and (j==0):
        ar[i][j] = m
        
    elif i == j:
        ar[i][j] = ar[i-1][j-1] + k
        
    elif i > j:
        ar[i][j] = ar[i-1][j] - 1
        
    else:
        ar[i][j] = ar[i][j-1] - 1

    return pagli(n, m, k, i, j+1)

ar = [[0]*n for _ in range(n)]
pagli(n,m,k)
for i in range(n):
    print(*ar[i])

'''
#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    ar = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i==0) and (j==0):
                ar[i][j] = m
                continue
            if i == j:
                ar[i][j] = ar[i-1][j-1] + k
                continue
            if i > j:
                ar[i][j] = ar[i-1][j] - 1
                continue
            if i < j:
                ar[i][j] = ar[i][j-1] - 1
                

    for i in range(n):
        print(*ar[i])

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
'''
