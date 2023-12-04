n, d = input().split()
n, d = int(n), int(d)
count = 0

inf = (2*(10**4)+1)
li = [0] * inf
for i in input().split():
    i = int(i)
    li[i] += 1

for i in range(inf-d-d):
    if li[i]:
        if li[i+d]:
            if li[i+d+d]:
                count += 1

print(count)
'''TLE

li = [int(p) for p in input().split()]

for i in range(n-2):
    temp = li[i]
    j = i+1
    while j<n:
        if li[j] == (temp+d):
            temp += d
            if temp == (li[i]+d+d):
                count += 1
                break

        j += 1

print(count)
'''
