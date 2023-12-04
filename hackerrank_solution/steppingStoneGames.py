import math

for _ in range(int(input().strip())):
    p = int(input().strip())
    p = math.sqrt(1+4*2*p)
    if p == int(p):
        p = (p-1)//2
        print('Go On Bob', int(p)+1)
    else:
        print('Better Luck Next Time')


#here S = (n*n+1)//2; ax^2+bx+c=0
