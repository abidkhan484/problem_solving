# intra cste programming contest replay 2017

def findGf():
    
    n = int(input().strip())
    n_bin = bin(n)
    length = len(n_bin)

    print('2^%d'%(length-3), end='')
    for i in range(3, length):
        if n_bin[i]=='1':
            print(' + 2^%d'%(length-i-1), end='')

for _ in range(int(input().strip())):
    findGf(); print()
