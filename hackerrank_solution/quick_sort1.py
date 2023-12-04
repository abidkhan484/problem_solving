def quicksort(li):
    pivot = li[0]
    l = len(li); t=l-1

    for i in range(t, 0, -1):
        if pivot <= li[i]:
            l -= 1
            li[l], li[i] = li[i], li[l]

    li[l-1], li[0] = li[0], li[l-1]
    return li

n = int(input().strip())
li = [int(_) for _ in input().split()]


li = quicksort(li)
for _ in li:
    print(_, end=' ')
