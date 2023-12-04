from random import randint

t = randint(1,5)
print(t)
for i in range(t):
    n = randint(3,200)
    k = randint(1,n)
    print('%d %d'%(n,k))
    for j in range(n):
        print(randint(-n, n), end=' ')
    print()
