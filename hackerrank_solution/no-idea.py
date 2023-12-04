from collections import Counter

n, m = map(int, input().split())

nList = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

nListCount = Counter(nList)
nList = set(nList)

matchingA = nList.intersection(A)
matchingB = nList.intersection(B)

earn = 0
loss = 0
for i in matchingA:
    if nListCount[i] > 1:
        earn += nListCount[i]
        continue
    earn += 1

for i in matchingB:
    if nListCount[i] > 1:
        loss += nListCount[i]
        continue
    loss += 1

print(earn-loss)

