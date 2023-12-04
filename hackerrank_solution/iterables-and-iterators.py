from itertools import combinations

n = int(input().strip())
combin = input().split()
m = int(input().strip())

combin = list(combinations(combin, m))
count = 0; length = len(combin)

for i in range(length):
    if 'a' in combin[i]:
        count += 1

print('%.4f' %(count/length))
