wh = int(input().strip())

my_dic=dict(input().split() for i in range(wh))

for i in range(wh):
    check = input().strip()
    for j in range(wh):
        if check in my_dic[check]:
            print (check+ "="+ my_dic)
            break
            
        else:
            print ("Not found")
            break
            
        j+=1
            
    i+=1
        
    
