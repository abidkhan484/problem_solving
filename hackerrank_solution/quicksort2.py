'''
def quick_sort(*ar):
    p, *a = ar
    first, last = [], []
    for i in a:
        if i < p:
            first.append(i)
        else:
            last.append(i)
    if len(first) > 1:
        first = quick_sort(*first)
        print(*first)
    if len(last) > 1:
        last = quick_sort(*last)
        print(*last)
    return first + [p] + last


n = int(input())
p, *a = map(int, input().split())
print(*quick_sort(p, *a))

############################################################################
'''
def quicksort_partition(li, end, start=0):

    p = li[start]
    j = end
    for i in range(end-1, start, -1):
        if li[i] > p:
            j -= 1
            li[i], li[j] = li[j], li[i]
    
    j -= 1
    li[start], li[j] = li[j], li[start]


    return j, li

def quicksort(li, end, start=0):

    position = 0
    left, right = [], []

    if end > start:
        position, li = quicksort_partition(li, end, start)
        if len(li[start:end]) > 1:
            left = quicksort_partition(li[start:position], position, start)
            print(*left)
            right = quicksort_partition(li[position+1:end], end, position+1)
            print(*right)
#        quicksort(li, position, start)
#        quicksort(li, end, position+1)

    return left + li[position] + right


#a = [1, 3, 9, 8, 2, 7, 5]
a = [5, 8, 1, 3, 7, 9, 2]
print(quicksort(a, 7))




