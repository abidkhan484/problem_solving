'''
# solved
n = int(input().strip())

li = []
d = dict()

for _ in range(n):
    m = input().strip()
    try:
        d[m] += 1
    except:
        d[m] = 1
        li.append(m)

print(len(li))
for i in li:
    print(d[i], end=' ')
'''

from collections import Counter

n = int(input().strip())
li = []
for _ in range(n):
    li.append(input().strip())

countList = Counter(li)
print(len(countList))
# it helps
for word in li:
    derp = countList.pop(word, None)
    if derp:
        print(derp, end=' ')

'''
# https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
'''
