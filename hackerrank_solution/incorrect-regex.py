import re

def checkValidation():
    try:
        print(bool(re.compile(input().strip())))
    except:
        print(False)
        
for _ in range(int(input().strip())):
    checkValidation()
