def checkGrid(i, j):
    x, y = 0, 0
    for p in range(i, i+r):
        for q in range(j, j+c):
            if ar[x][y] != grid[p][q]:
                return False
            y += 1
        x += 1; y = 0
    return True

for _ in range(int(input().strip())):
    
    row, col = map(int, input().split())
    grid = [input().strip() for _ in range(row)]
    r, c = map(int, input().split())
    ar = [input().strip() for _ in range(r)]

    counter = 0
    for i in range(row-r+1):
        for j in range(col-c+1):
            if checkGrid(i, j):
                print('YES')
                counter = 1
                break
    if not counter:
        print('NO')


'''
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
'''
