import re

s = int(input().strip())

li = []
R = r'<'
for _ in range(s):
    string = input()
    while string:
        a = re.search(R, string)
        if not a:
            break
        a = a.start() + 1
        temp = ''
        while True:
            if string[a]==' ':
                a += 1
                continue
            
