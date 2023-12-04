# easy problem; i just using counting sort to solve this

m, n = map(int, input().split())

ar = [0]*n
for i in range(m):
    p, r = map(int, input().split())
    ar[p-1] += r

avg = sum(ar)//n
print(1, (ar[0]-avg+(avg*n)-sum(ar)))
for i in range(1, n):
    print(i+1, ar[i]-avg)
