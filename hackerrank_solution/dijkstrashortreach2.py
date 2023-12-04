# the problem is not solved yet

from heapq import heappush, heappop

class Node:

    def __init__(self, first, sec, data):
        self.data = data
        self.first = first
        self.sec = sec

    def __repr__(self):
        return repr(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __add__(self, other):
        return self.data + other.data


def updateList(data, st):

    if ajlist[st]=='p':
        return
    m, n = data.first-1, data.sec-1

    if (st==m) and (final[n] > data.data + final[m]):
        if ajlist[n]=='p':
            return
        final[n] = data.data + final[m]
        return
    if (st==n) and (final[m] > data.data + final[n]):
        if ajlist[m]=='p':
            return
        final[m] = data.data + final[n]
        return

def updateHeap(m):
    if ajlist[m]=='p':
        return
    for i in range(len(ajlist[m])):
        if ajlist[m][i] not in heap:
            heappush(heap, ajlist[m][i])
            updateList(ajlist[m][i], ajlist[m][i].first-1)
            updateList(ajlist[m][i], ajlist[m][i].sec-1)

for _ in range(int(input().strip())):
    inf = 10**5+1
    heap = []
    n, m = map(int, input().split())

    final = [inf for _ in range(n)]
    ajlist = [[] for _ in range(n)]
    for _ in range(m):
        p, r, i = map(int, input().split())
        node = Node(p, r, i)
        ajlist[p-1].append(node)
        ajlist[r-1].append(node)

    start = int(input().strip())-1
    final[start] = 0

    for i in range(len(ajlist[start])):
        heappush(heap, ajlist[start][i])
        updateList(ajlist[start][i], start)
    ajlist[start] = 'p'

    while heap:
        data = heappop(heap)
        p, r = data.first-1, data.sec-1
        updateHeap(p); updateHeap(r)
        ajlist[p] = 'p'; ajlist[r] = 'p'

    for i in range(n):
        if final[i]==inf:
            final[i] = -1
        if not final[i]:
            continue
        print(final[i], end=' ')

    print()

'''
def push(data):
    heap.append(data)
    length = len(heap)-1
    
    while length:
        par = (length-1)>>1
        if heap[par] > data:
            heap[length] = heap[par]
            length = par
            continue
        break
    heap[length] = data

def _siftdown(pos):
    length = len(heap)
    item = heap[pos]
    leftchild = (2*pos)+1
    while leftchild < length:
        rightchild = leftchild + 1
        if rightchild < length and heap[leftchild] > heap[rightchild]:
            leftchild = rightchild
        if item.data < heap[leftchild].data:
            break
        heap[pos] = heap[leftchild]
        pos = leftchild
        leftchild = (2*pos) + 1
    heap[pos] = item

def pop():
    length = len(heap)-1
    if not length:
        return heap.pop()
    heap[0], heap[length] = heap[length], heap[0]
    item = heap.pop()
    _siftdown(0)
    return item
'''
