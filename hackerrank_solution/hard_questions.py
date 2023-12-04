def hard(pr, ia, n):
    if pr==ia:
        return 0
    count = 0
    for i in range(n):
        if (pr[i]==ia[i]) or (pr[i]=='.') or (ia[i]=='.'):
            count += 1

    return count

n = int(input().strip())

pr = input().strip()
ia = input().strip()

print(hard(pr, ia, n))
