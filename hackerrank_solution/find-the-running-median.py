from heapq import heappush, heappop

# use heapq as maximum priority queue; this tutorial is from
# "https://mail.python.org/pipermail/python-list/2009-March/530818.html"
class Backwards(int):
    def __lt__(self, other):
        return not int.__le__(self, other)
    def __le__(self, other):
        return not int.__lt__(self, other)
    def __gt__(self, other):
        return not int.__ge__(self, other)
    def __ge__(self, other):
        return not int.__gt__(self, other)

minheap = []
minlen, maxlen = 0, 0
maxheap = []
median = -1
for _ in range(int(input().strip())):
    item = int(input().strip())
    if item > median:
        heappush(minheap, item)
        minlen += 1
    else:
        heappush(maxheap, Backwards(item))
        maxlen += 1
    
    if (maxlen-minlen) > 1:
        temp = heappop(maxheap)
        temp = int(temp)
        maxlen -= 1
        minlen += 1
        heappush(minheap, temp)
    elif (minlen-maxlen) > 1:
        temp = heappop(minheap)
        minlen -= 1
        maxlen += 1
        heappush(maxheap, Backwards(temp))

    if maxlen==minlen:
        median = (maxheap[0]+minheap[0])/2
        print('%.1f' %median)
    elif maxlen > minlen:
        print('%.1f' %maxheap[0])
        median = int(maxheap[0])
    else:
        print('%.1f' %minheap[0])
        median = minheap[0]



'''
# i just try to solve the problem using insertion sort idea
heap = []; length = -1
for _ in range(int(input().strip())):
    data = int(input().strip())
    heap.append(data)
    length += 1
    i = length
    while i:
        if heap[i-1] > data:
            heap[i] = heap[i-1]
            i -= 1
            continue
        break
    heap[i] = data

    # now the list-heap is already sorted
    p = length >> 1
    if length & 1:
        print('%.1f' %((heap[p]+heap[p+1])/2))
    else:
        print('%.1f' %heap[p])

'''

