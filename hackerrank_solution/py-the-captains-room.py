from collections import Counter

k = int(input().strip())
roomNo = input().split()

counter = Counter(roomNo)
for i in counter:
    if counter[i] != k:
        print(i)
        break
