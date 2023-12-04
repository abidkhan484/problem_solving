'''
# i can solve this problem different way
# but i try to solve it using python package

from collections import Counter

n = int(input().strip())
arr = [int(p) for p in input().split()]

p = Counter(arr)
for i in p.keys():
    if p[i]==1:
        print(i)
        break

'''
# here is another process to complete the task
# idea from editorial

n = int(input().strip())
arr = [int(p) for p in input().split()]

res = 0
for i in range(n):
    # here ^ is the xor notation
    res = (res ^ arr[i])

print(res)
