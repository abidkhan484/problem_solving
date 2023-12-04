# intra cste programming contest replay 2017

def kitty():

    pagli = input().split()

    llst = len(pagli[0]); rlst = len(pagli[1])
    if rlst==min(llst, rlst):
        i = rlst; j=llst
        lst = list(pagli[1]); rst = list(pagli[0])
    else:
        i=llst; j = rlst
        lst = list(pagli[0]); rst = list(pagli[1])

    count = 0
    while i:
        p = j
        while p:
            if lst[i-1]==rst[p-1]:
                count += 1
                rst[p-1] = -1
                break
            p -= 1
        i -= 1

    return llst+rlst-(2*count)
    

for i in range(int(input().strip())):
    print('Case %d:' %(i+1), kitty())
