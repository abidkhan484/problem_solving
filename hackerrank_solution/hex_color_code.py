import re
'''
n =  int(input().strip())
li = []
for i in range(n):
    temp = input()
    li.append(temp)
    
string = ''.join(li)
'''
string = '#BED{    color: #FfFdF8; background-color:#aef;    font-size: \
            123px;    background: -webkit-linear-gradient(top, #f9f9f9, #fff);}\
            #Cab{    background-color: #ABC;    border: 2px dashed #fff;} '
R = r'#[A-Fa-f0-9]{3}'
r = re.findall(R,string)

