def printTime(s1, s2, pt):
    print(s1, pt, s2)
    
def checkTime(a):
    if a==1:
        string = 'one minute'
    elif a==15:
        string = 'quarter'
    else:
        if a <= 20:
            string = dic[a]+' minutes'
        else:
            string = 'twenty ' + dic[a%20] + ' minutes'
    return string

dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
       8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
       14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
       19:'nineteen'
       }

hour = int(input().strip())
minute = int(input().strip())
if minute < 30:
    if not minute:
        print(dic[hour] + ' o\' clock')
    else:
        string = checkTime(minute)
        printTime(string, dic[hour], 'past')
elif minute > 30:
    minute = 60 - minute
    hour = (hour+1) % 12
    if not hour:
        hour = 12
    string = checkTime(minute)
    printTime(string, dic[hour], 'to')
else:
    print('half past', dic[hour])
