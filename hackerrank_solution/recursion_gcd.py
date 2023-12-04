'''
there is a fun in gcd. when i try to get gcd of two numbers. its no matter
which one(larger or smaller), i passed to the function first. that means
gcd(34, 22)==gcd(22, 34)
'''
#!/bin/python3

import sys

# return gcd using recursion
def gcd(a, b):
    rem = a%b
    # base case
    if rem:
        return gcd(b, rem)

    return b


# return gcd from a list using recursion
def gcd_list(li):
    l = len(li)
    temp_gcd = []

    #loop to pass two arguments to the gcd(a, b) function
    for i in range(1, l):
        temp_gcd.append(gcd(li[i], li[i-1]))

    # try to make a recursion of the above loop
    return temp_gcd[-1]


print(gcd(60, 44))
print(gcd_list([12,24,36,48,52]))
