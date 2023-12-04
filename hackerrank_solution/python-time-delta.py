from datetime import datetime

def timeDelta():
    t1 = datetime.strptime(input().strip(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input().strip(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((t1-t2).total_seconds())))

for _ in range(int(input().strip())):
    timeDelta()
