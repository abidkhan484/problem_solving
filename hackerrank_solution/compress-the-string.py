import itertools

group = itertools.groupby(input().strip())
li = []

for k, g in group:
    # k = int(k)
    # g = len(list(g))
    li.append((len(list(g)), int(k)))

print(*li)
