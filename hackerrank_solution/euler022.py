ar = []
for _ in range(int(input().strip())):
    ar.append(input().strip())

ar.sort()

for _ in range(int(input().strip())):
    var = input().strip()
    val = ar.index(var)+1
    total = 0
    for i in var:
        total += (ord(i)-64)
    print(total*val)
