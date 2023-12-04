for _ in range(int(input().strip())):

    n, k, x, d = map(int, input().split())
    arr = [int(p) for p in input().split()]

    total = 0
    for i in range(n):
        total += max(k, ((x*arr[i])/100))

    print('upfront') if total > d else print('fee')
