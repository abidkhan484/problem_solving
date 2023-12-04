def add(p):
    mylist.append(p)
    length = len(mylist)-1
    # this part of the code just organise the element
    # according to the algorithm (bottom to top)
    while length:
        par = (length-1)>>1
        if mylist[par] > p:
            mylist[length] = mylist[par]
            length = par
            continue
        break
    mylist[length] = p


def move_to_top(pagli):
    # this loop moves the element to the Top
    i = pagli
    while pagli:
        par = (i-1)//2
        if mylist[par] > mylist[pagli]:
            mylist[pagli], mylist[par] = mylist[par], mylist[pagli]
            pagli = par
        else:
            break

def move_to_down(i):
    # this one Down the element
    length = len(mylist)
    item = mylist[i]
    childpos = (2*i)+1
    while childpos < length:
        rightpos = childpos + 1
        if rightpos < length and not mylist[childpos] < mylist[rightpos]:
            childpos = rightpos
        mylist[i] = mylist[childpos]
        i = childpos
        childpos = (2*i)+1
    mylist[i] = item


def delete(p):
    length = len(mylist)
    for i in range(length-1):
        if mylist[i]==p:
            mylist[i], mylist[-1] = mylist[-1], mylist[i]
            mylist.pop()
            break
    else:
        mylist.pop()
        return


    move_to_down(i)
    move_to_top(i)


def printMin():
    print(mylist[0])

mylist = []; items = set()
'''add(234);add(252);add(273);add(492); add(85)
print(mylist)
delete(6)
print(mylist)'''

for _ in range(int(input().strip())):
    li = list(map(int, input().split()))
    if li[0]==1:
        add(li[1])
        items.add(li[1])
    elif li[0]==2:
        items.remove(li[1])
    else:
        while mylist[0] not in items:
            delete(mylist[0])
            
        printMin()

'''another nice solution using heapq library:

from heapq import *
heap, items = [], set()
for _ in range(int(input())):
    w = list(map(int, input().split()))
    if w[0] == 1:
        heappush(heap, w[1])
        items.add(w[1])
    elif w[0] == 2:
        items.remove(w[1])
    else:
        while heap[0] not in items:
            heappop(heap)
        print(heap[0])'''

'''input:
22
1 286789035
1 255653921
1 274310529
1 494521015
3
2 255653921
2 286789035
3
1 236295092
1 254828111
2 254828111
1 465995753
1 85886315
1 7959587
1 20842598
2 7959587
3
1 -51159108
3
2 -51159108
3
1 789534713'''
