# this problem is not solved yet
# project euler 018

def maximumPathSum():
    
    row = int(input().strip())
    ar = [[int(p) for p in input().split()] for i in range(row)]

    tmp = row-1
    for i in range(row-1, 0, -1):
        j = 0; p = i
        while j < tmp:
            ar[i-1][j] += max(ar[i][j], ar[i][j+1])
            j += 1
        tmp -= 1

    print(ar[0][0])

for _ in range(int(input().strip())):
    maximumPathSum()


'''
def maximumPathSum():
    ar = [[int(p) for p in input().split()] for i in range(int(input().strip()))]

    row = len(ar); maxim = -1
    # check total for all left diagonal
    for i in range(row):

        j = 0; total = 0
        while j < i:
            total += ar[j][j]
            j += 1

        j = i
        while j < row:
            total += ar[j][i]
            j += 1

        if total > maxim:
            maxim = total


    # this checking is for right diagonal
    tmp = row - 1
    for i in range(1, row-1):

        j = 0; total=0
        while j < i:
            total += ar[j][0]
            j += 1
            
        j=0; p=i
        while j < tmp:
            total += ar[p][j]
            p += 1; j += 1
        tmp -= 1

        if total > maxim:
            maxim = total

    print(maxim)

for i in range(int(input().strip())):
    maximumPathSum()
    


another way to total all left diagonal
tmp = row
for i in range(row):
    j=0; p=i; total=0
    while j < tmp:
        #print(ar[p][i],end=' ')
        total += ar[p][i]
        p += 1; j += 1
    tmp -= 1

    #print()
    if total > maxim:
        maxim = total

'''
