n = int(input().strip())


array = list(map(int, input().split()))
j = array[n-1]
for i in range(n-2, -1, -1):
    #print(i)
    if (array[i] > j):
        array[i+1] = array[i]
        for p in range(n):
            print(array[p], end =' ')
    
    else:
        #print(i, array[i])
        array[i+1] = j
        for p in range(n):
            print(array[p], end=' ')
            
        break
    print()

#print(i)
if (array[0]==array[1]):
    array[0] = j
    for i in range(n):
        print(array[i], end=' ')
