string = input().strip()
k = int(input().strip())
n = len(string)
i = 0; sp = n//k;  j = k

while i < n:
    li = []; st = string[i:j]
    for p in st:
        if p not in li:
            li.append(p)
    print(''.join(li))
    i += k; j += k    
