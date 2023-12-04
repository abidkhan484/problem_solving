n = int(input().strip())
mylist = [[] for _ in range(100)]
idx = []

for _ in range(n):
    m, a = input().split()
    m = int(m)
    idx.append(m)
    mylist[m].append(a)

for i in range(100):
    if mylist[i]:
        mylist[i].reverse()

pri = ['-'] * (n//2)
for i in range(n//2):
    mylist[idx[i]].pop()

for i in range(n//2, n):
    pri.append(mylist[idx[i]].pop())

del mylist
mylist = [[] for _ in range(100)]
for i in range(n):
    mylist[idx[i]].append(pri[i])

del idx
pri = []
for i in range(100):
    if mylist[i]:
        pri.extend(mylist[i])

print(*pri)

'''
input:
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

output:
- - - - - to be or not to be - that is the question - - - -
'''
