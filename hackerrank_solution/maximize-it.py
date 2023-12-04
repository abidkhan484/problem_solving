# the problem is not solved yet

from itertools import product

k, m = map(int, input().split())

li = []
for _ in range(k):
    pagli = list(map(int, input().split()))
    pagli.pop(0)
    li.append(pagli)

maxim = -1
li = list(product(*li))
l = len(li[0])
for i in range(len(li)):
    total = 0
    for p in range(l):
        total += (li[i][p]**2)
    total = total % m
    if total > maxim:
        maxim = total

print(maxim)    
