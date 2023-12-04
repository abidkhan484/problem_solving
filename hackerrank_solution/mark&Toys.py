n, m = map(int, input().split())
items = list(map(int, input().split()))

items.sort()

for i in range(n):
    m -= items[i]
    if m < 0:
        print(i)
        break
else:
    print(n)
