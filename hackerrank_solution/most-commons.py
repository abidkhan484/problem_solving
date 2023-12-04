from collections import Counter

string = input().strip()
d = Counter(string)

for _ in range(3):
    maxim = -1
    for k, v in d.items():
        if (v > maxim) or (v == maxim and k < item):
            maxim = v
            item = k
    d.pop(item)
    print(item, maxim)

