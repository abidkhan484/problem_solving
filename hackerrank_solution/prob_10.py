sample=int(input())

bin_val = bin(sample)[2:]
x = len(bin_val)
count1, count2 = 0, 0
while(x):
    if bin_val[x-1] is '1':
        count1+=1
    else:
        if(count2 < count1):
            count2=count1
        count1=0
    x-=1
if (count2>count1):
    print(count2)
else:
    print(count1)
