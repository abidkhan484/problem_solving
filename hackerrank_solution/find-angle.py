import math

m = int(input().strip())
n = int(input().strip())

angle = math.degrees(math.atan(m/n))
temp = (math.floor(angle) + (math.floor(angle)+1))/2
if angle >= temp:
    angle = int(angle) + 1
else:
    angle = int(angle)
print('%d°' %angle)
