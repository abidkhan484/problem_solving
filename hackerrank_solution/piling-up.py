from collections import deque

for _ in range(int(input().strip())):

    n = int(input().strip())
    d = deque(map(int, input().split()))

    maxim = 2**31+1
    while d:
        if (d[0] > d[-1]) and (maxim >= d[0]):
            maxim = d.popleft()
        elif (d[0] <= d[-1]) and (maxim >= d[-1]):
            maxim = d.pop()
        else:
            break
    print('No') if d else print('Yes')

# see, there's a nice solution in the editorial
