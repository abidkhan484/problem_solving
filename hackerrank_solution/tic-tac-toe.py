player1 = input('type your(player1) name: ').strip()
player2 = input('type your(player2) name: ').strip()


'''
game_dict = {'top-L':None, 'top-M':None, 'top-R':None,
             'mid-L':None, 'mid-M':None, 'mid-R':None,
             'low-L':None, 'low-M':None, 'low-R':None}
'''
li = 9*[None]; p = 0
p1_opt, p2_opt = 'X', 'O'
player = None

while True:

    if li.count(None)==0:
        break
    
    if not (p & 1):
            player = player1
            sign = p1_opt
    else:
            player = player2
            sign = p2_opt

    opt = int(input('Enter your option between 1 to 9'+'\n'
                    +'Input for %s ' %player).strip())

    while True:
        if not ((opt > 0) and (opt < 10)):
            print('Please, Enter your option between 1 to 9')
            opt = int(input('Input for %s ' %player).strip())
            continue
        
        elif(li[opt-1]==p1_opt) or (li[opt-1]==p2_opt):
            print('Your option is already for \'%s\'' %player)
            opt = int(input('Input for %s ' %player).strip())
            continue

        p += 1
        break
        
    li[opt-1] = sign

    if opt==1:

        if ((li[opt-1]==li[1]) and (li[opt-1]==li[2])) or ((li[opt-1]==li[3]) and (li[opt-1]==li[6])) or ((li[opt-1]==li[4]) and (li[opt-1]==li[8])):
            print('%s wins!', player)
            break
        else:
            continue
    elif opt==2:
        
        if ((li[1]==li[0]) and (li[1]==li[2])) or ((li[1]==li[4]) and (li[1]==li[7])):
            print('%s wins!', player)
            break
        else:
            continue
    elif opt==3:
        
        if ((li[2]==li[1]) and (li[0]==li[2])) or ((li[2]==li[5]) and (li[opt-1]==li[7])):
            print('%s wins!', player)
            break
        else:
            continue
    elif opt==2:
        
        if ((li[1]==li[0]) and (li[1]==li[2])) or ((li[1]==li[4]) and (li[opt-1]==li[7])):
            print('%s wins!', player)
            break
        else:
            continue
