import re

R = r'([\da-zA-Z])\1'
a = re.search(R,input())

if a:
    print(a.group(1))
else:
    print(-1)
