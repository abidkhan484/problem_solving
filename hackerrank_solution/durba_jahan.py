# intra cste programming contest replay 2017

def durbaTest():

    n = int(input().strip())
    arr = [int(p) for p in input().split()]

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return 'NO'

        tmp = arr[i] ^ arr[i+1]
        if tmp < 2:
            return 'NO'

    return 'YES'

for i in range(int(input().strip())):
    print('Case #%d:'%(i+1), durbaTest())
