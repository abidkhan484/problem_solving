def checkCavity(i, j):
    if (i-1 < 0) or (i+1 == n) or (j-1 < 0) or (j+1 == n):
        return False
    if (li[i][j] > li[i-1][j]) and (li[i][j] > li[i+1][j]) and (li[i][j] > li[i][j-1]) and (li[i][j] > li[i][j+1]):
        return True
    return False

li = []
n = int(input().strip())
for _ in range(n):
    li.append([int(p) for p in input().strip()])

arr = []
for i in range(n):
    t = []
    for j in range(n):
        if checkCavity(i, j):
            t.append('X')
            continue
        t.append(str(li[i][j]))
    arr.append(t)
    

for i in range(n):
    print(''.join(arr[i]))
