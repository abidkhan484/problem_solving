def quicksort(li):
    pivot = li[0]
    l = len(li); t = l-1

    for i in range(l-1, -1, -1):
        if pivot >= li[i]:
            temp = li[i]
            li[i] = li[t]
            li[t] = temp
            print(li)
            t -= 1
            
    li[j] = pivot

    return li


n = int(input().strip())
li = [int(c) for c in input().split()]

li = quicksort(li)
for _ in li:
    print(_, end=' ')
