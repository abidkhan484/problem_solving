def find_difference(n, i, k):

    p, r = k-i, n-k-1
    if p == min(p, r):
        #position is from the start
        j = p; posi = 0
    else:
        #position is from the end
        j = r; posi = 1

    return j, posi


def reverse_game(n, k):

    for i in range(n):
        j, posi = find_difference(n+1, i, k)

        if k < i:
            return k

        if not posi:
            k = n-j
        else:
            k = i+j

    return k
        
    
#t = int(input().strip())
#n,k = input().strip().split(' ')
n,k = 5, 2
print(reverse_game(n-1, k))
n,k = 3, 1
print(reverse_game(n-1, k))
n, k = 8, 6
print(reverse_game(n-1, k))

'''
complexity:  O(1)


for _ in range (int(input().strip())):
    n,k = [int(x) for x in input().split()]
    if k<n/2:
        print 2*k+1
    else:
        print (n-1-k)*2
'''
