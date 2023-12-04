def decentNumber(n):

    if n < 3:
        print(-1)
        return

    fives = n-(n%3)
    threes = n-fives

    if not threes:
        print('5'*n)
        return

    while threes < n:
        if not (threes % 5):
            break
        fives -= 3
        threes += 3

    if not fives and not (threes%5):
       print('3'*threes)
       return

    if not fives:
        print(-1)
        return

    print(fives*'5'+'3'*threes)


for _ in range(int(input().strip())):
    decentNumber(int(input().strip()))


'''
# input:
4
1
3
5
11'''
