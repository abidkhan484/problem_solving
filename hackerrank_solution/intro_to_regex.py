import re


n = int(input().strip())
for _ in range(n):
    r = r'^[+-]?\d*\.\d+$'
    a = input()
    if a=='0':
        print('False')
        continue
    x = re.search(r, a)
    print(bool(x))
