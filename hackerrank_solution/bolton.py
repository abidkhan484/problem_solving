# codemash '17 replay

def feel(m):
    if m==1:
        print('*')
        return
    print('*' * m)
    for i in range(m-2):
        print('*',end='')
        print(' '*(m-2), end='')
        print('*')
    print('*' * m)

for _ in range(int(input().strip())):
    feel(int(input().strip()))
