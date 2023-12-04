# editorial solution
n, s = map(int, input().split())

jl = {}
def jumpl(x):
    x -= 1
    return jl.get(x, x)

jr = {}
def jumpr(x):
    x += 1
    return jr.get(x, x)

for i in range(s):
    l, r = map(int, input().split())
    L = jumpl(l)
    R = jumpr(r)
    print ((r * (r + 1) - l * (l - 1)) // 2 + (0 <= L < n) * L + (0 <= R < n) * R)
    L = jumpl(L)
    R = jumpr(R)
    jr[L + 1] = R
    jl[R - 1] = L

'''input:
10 3
2 4
6 7
9 9

output:
15
21
9

'''

'''
# the problem is not solved yet

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def insert(self, node):
        root = Node(0)
        curr = root
        for i in range(1, node+1):
            item = Node(i)
            curr.next = item
            curr = curr.next
        return root

    def delete(self, root, start, end):
        summation = 0; pre = root; N = end-start+1
        curr = root; prev = curr.next; curr = curr.next.next
        if pre.data==start:
            summation += (N*(2*start+end-start))//2
            p = N
            while p:
                pre = pre.next
                p -= 1
            if pre:
                summation += pre
                print(summation)
                return pre.next
        elif prev.data = start:
            summation += pre.data
            summation += (N*(2*start+end-start))//2
            
            
        while curr.next:
            if curr.next.data==start:
                break
            prev = prev.next
            curr = curr.next
        
        if prev.data==start:
            summation += 0
        else:
            summation += prev.data
        summation += (N*(2*start+end-start))//2
        

n, s = map(int, input().split())


# this got runtime error naturally
ar  = [1]*n
for _ in range(s):
    start, end = map(int, input().split())
    summation = ((end-start+1)*(2*start+end-start))//2

    for i in range(start-1, 0, -1):
        if ar[i]:
            summation += i
            ar[i] = 0
            break
    for i in range(end+1, n):
        if ar[i]:
            summation += i
            ar[i] = 0
            break
    for i in range(start, end+1):
        ar[i] = 0

    print(summation)
'''
