from collections import Counter

x = int(input().strip())
shoes = Counter([int(p) for p in input().split()])

n = int(input().strip())
total = 0
for _ in range(n):
    m, n = map(int, input().split())
    if shoes[m]:
        shoes[m] -= 1
        total += n
print(total)
