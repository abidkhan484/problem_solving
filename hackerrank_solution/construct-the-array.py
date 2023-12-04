# the problem is not solved yet

import math
def ncr(n,r):
    f = math.factorial
    return f(n)//f(r)//f(n-r)

'''
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom
'''
def countArray(n, k, x):
    return ncr(k, n-x)

if __name__ == "__main__":
    n, k, x = input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArray(n, k, x)
    print(answer)

