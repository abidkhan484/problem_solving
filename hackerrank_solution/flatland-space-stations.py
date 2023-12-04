def towerTerminate(pos):
    p = 1
    for i in range(pos + 1, n):
        dis[i] = p
        p += 1

def towerPosition(pos):
    for i in range(pos, n):
        if ar[i]:
            return i
    return -1

n, m = map(int, input().split())
ar = [0] * n
dis = [0] * n

for i in input().split():
    i = int(i)
    ar[i] = 1

tower1 = towerPosition(0)
for i in range(tower1 + 1):
    dis[i] = tower1 - i
dis[tower1] = 0
tower2 = towerPosition(tower1 + 1)
while tower2 != -1:
    for i in range(tower1+1, tower2):
        if (i-tower1) > (tower2-i):
            dis[i] = tower2-i
        else:
            dis[i] = i-tower1
    tower1 = tower2
    dis[tower2] = 0
    tower2 = towerPosition(tower2+1)

towerTerminate(tower1)
maxim = -1
for i in range(n):
    if dis[i] > maxim:
        maxim = dis[i]
print(maxim)
