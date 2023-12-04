import re

# this solution can make overlapping
p = input()
regex = r'(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])'


li = re.findall(regex,p)

if li:
    for i in li:
        print(i)
else:
    print('-1')
