# try to make it using class(Object Oriented)

from heapq import heappush, heappop

def makeTimeHeap(maxTime):
    
    while heap and (maxTime > heap[0][0]):
        m, n = heappop(heap)
        heappush(timePrior, [n,m])

def makeTotal(currTime, total):

    n, m = timePrior[0]
    currTime = currTime+n
    total += (currTime-m)
    return currTime, total

p = int(input().strip())
inf = 10**9+1
heap = []; timePrior = []
for _ in range(p):
    m, n = map(int, input().split())
    heappush(heap, [m,n])


total = 0
while heap or timePrior:
    if not timePrior:
        m, n = heappop(heap)
        heappush(timePrior, [n,m])
        currTime = m
        continue
    
    currTime, total = makeTotal(currTime, total)
    heappop(timePrior)
    makeTimeHeap(currTime)


print(total//p)


'''
5
961148050 385599125
951133776 376367013
283280121 782916802
317664929 898415172
980913391 847912645
'''
