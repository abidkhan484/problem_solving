import math

string = ''.join(input().split())
length = len(string)

col = math.ceil(math.sqrt(length))
'''if not (length%col):
    row = length//col
else:
    row = (length//col) + 1
'''
row = col
i = 0
while i < row:
    j = i; t = ''
    while j < length:
        t += string[j]
        j += col
    print(t, end=' ')
    i += 1

'''
i = 0; tmp = col; li = []
for _ in range(row):
    li.append(string[i:tmp])
    i += col; tmp += col

mylist = []; st = string
for i in range(col):
    string = ''
    for j in range(row):
        try:
            string += li[j][i]
        except:
            pass
    mylist.append(string)
    
print(*mylist)
'''
