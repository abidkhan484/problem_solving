# the problem is not solved yet

from fractions import Fraction
from functools import reduce

def product(fracs):

    if len(fracs)==1:
        return [fracs[0].numerator, fracs[1].denominator]
    for i in range(1, len(fracs)):
        fracs[i] *= fracs[i-1]
    '''
    editorial solution:
    
    t = reduce(lambda x, y : x*y, fracs)
    return t.numerator, t.denominator
    '''
    return [fracs[-1].numerator, fracs[-1].denominator]

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
