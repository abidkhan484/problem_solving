cube = lambda x: x**3

def fibonacci(n):
    t=[]
    i=0, j = 1
    while (n>0) and (i<=n):
        t.append(i)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
