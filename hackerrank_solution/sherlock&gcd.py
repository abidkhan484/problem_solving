# this problem is still unsolved

def gcd(a):

    l = len(a)
    a.sort()
    for i in range(1, l):
        
        while a[i-1] != 0:
            mod = a[i-1]
            temp = a[i-1]            
            a[i-1] = a[i] % a[i-1]
            a[i] = temp

        a[i] = mod
        if mod==1:
            return 1
        
    return a[i]

#def checkFunction():
    
n = int(input().strip())
arr = [int(p) for p in input().split()]

res = gcd(arr)

if (res in arr) and (res != 1):
    print()
