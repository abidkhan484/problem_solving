def loveChe():
    
    n = int(input().strip())
    check = n//4
    arr = [int(p) for p in input().split()]

    i = 0; total=0; j=0
    while i < check:

        total += arr[i]
        i += 1

    prev = total; ch = check
    while j<3:
        total = 0; check += ch
        while i < check:
            total += arr[i]
            i += 1
        if prev != total:
            return 'NO'
        j += 1

    return 'YES'

for i in range(int(input().strip())):
    print('Case #%d:'%(i+1), loveChe())
