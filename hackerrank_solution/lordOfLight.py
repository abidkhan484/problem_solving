# codemash '17 replay

mylist = ['abcdef', 'bc', 'abdeg', 'abcdg', 'bcfg', 'acdfg', 'acdefg', 'abc', 'abcdefg', 'abcdfg']

pagli = int(input().strip()); i=0
while i < pagli:
    x = input().strip()
    if not x:
        continue
    print('Case %d:' %(i+1), mylist[int(x)])
    i += 1
