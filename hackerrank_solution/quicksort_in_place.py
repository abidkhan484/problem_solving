def quicksort_partition(li, end, start):

    p = li[end-1]
    j = start-1
    for i in range(start, end-1):
        if li[i] < p:
            j += 1
            li[i], li[j] = li[j], li[i]
    
    j += 1
    li[end-1], li[j] = li[j], li[end-1]

    print(*li)
    return j

def quicksort(li, end, start=0):

    position = 0
    if (end-start) > 1:
        position = quicksort_partition(li, end, start)
        quicksort(li, position, start)
        quicksort(li, end, position+1)

    return li

n = int(input().strip())
ar = list(map(int, input().split()))
quicksort(ar, n)

'''
input:
7
1 3 9 8 2 7 5

output:
1 3 2 5 9 7 8
1 2 3 5 9 7 8
1 2 3 5 7 8 9
'''
