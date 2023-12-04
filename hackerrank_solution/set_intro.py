def average(array):
    array=list(set(array))
    l=len(array)
    total=0
    
    for i in range(l):
        total+=array[i]

    return total/l

​if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
