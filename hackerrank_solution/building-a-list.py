#def buildingList():

st = '''a
ab
abc
abcd
abcde
abce
abd
abde
abe
ac
acd
acde
ace
ad
ade
ae
b
bc
bcd
bcde
bce
bd
bde
be
c
cd
cde
ce
d
de
e'''

n = 5 #int(input().strip())
ar = 'abcde' #input()

dic={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key in st:
    try:
        print(dic[key], end=' ')
    except:
        if key=='\n':
            print()


'''
for i in range(n):
    p = i+1; pagli = i+1
    print(ar[i])
    while p < n:
        st = ar[i]
        j = pagli
        
        while j < n:
            st += ar[j]
            print(st)
            j += 1

        p += 1
        pagli += 1

#for _ in range(int(input().strip())):
#    buildingList()
'''
'''input:
1
5
abcde

output:
a
ab
abc
abcd
abcde
abce
abd
abde
abe
ac
acd
acde
ace
ad
ade
ae
b
bc
bcd
bcde
bce
bd
bde
be
c
cd
cde
ce
d
de
e'''
