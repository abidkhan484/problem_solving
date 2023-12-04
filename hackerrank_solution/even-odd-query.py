def find(x, y):
    if x>y:
        return 1
    ans = pow(ar[x], find(x+1, y))
    return ans

n = int(input().strip())
ar = [int(x) for x in input().split()]

for _ in range(int(input().strip())):
    m, n = map(int, input().split())
    if not find(m-1, n-1) & 1:
        print('Even')
    else:
        print('Odd')
