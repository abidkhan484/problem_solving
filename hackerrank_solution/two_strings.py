for _ in range(int(input().strip())):
    print('YES') if set(input().strip()).intersection(set(input().strip())) else print('NO')
