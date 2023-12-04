from cmath import polar

li = input().split('+')
if len(li)==1:
    li = li[0].split('-')

    if len(li)==3:
        m = '-' + li[1]
        n = '-' + li[2]
    else:
        m = li[0]
        n = '-' + li[1]
else:
    m, n = li

m = int(m.strip()); n = int(n.strip()[:-1])

for p in polar(complex(m, n)):
    print(p)

'''
for p in polar(complex(input().strip())):
    print(p)

'''
