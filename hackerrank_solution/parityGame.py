'''
My Solution:

def smallestSizeSubsequence(n, ar):

    if not (sum(ar)&1):
        return 0

    c = 0
    for i in range(n):
        if ar[i]&1:
            c += 1

    if (not c) or (len(ar)==1):
        return -1

    return 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = smallestSizeSubsequence(n, ar)
print(result)
'''

# one liner solution
print((-1)**(int(input().strip()) < 2) * (sum(map(int, input().split())) % 2))
