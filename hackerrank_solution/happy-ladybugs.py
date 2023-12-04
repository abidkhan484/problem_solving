# the problem is not solved yet

from collections import Counter

for _ in range(int(input().strip())):
    n = int(input().strip())
    string = input().strip()
    counter = 0

    for i in range(n-1):
        if string[i] != string[i+1]:
            if i < n-2:
                if string[i+1] != string[i+2]:
                    break
            else:
                print('NO')
                counter = 1
                continue
    if counter:
        continue
    dictionary = Counter(string)
    if not dictionary['_']:
        print('NO')
        continue
    del dictionary['_']

    for item in dictionary:
        if dictionary[item] <= 1:
            print('NO')
            break
    else:
        print('YES')
