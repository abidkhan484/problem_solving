def facto(x):
    if(x<=0):
        return 1
    else:
        result=1
        result = x * facto(x-1)
        return result

user_input = int(input().strip())
print(facto(user_input))
