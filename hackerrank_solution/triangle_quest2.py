for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (round(i*(10**(i-1)))+round((i-1)*(10**(i-2)))+round((i-2)*(10**(i-3)))+round((i-3)*(10**(i-3))))
