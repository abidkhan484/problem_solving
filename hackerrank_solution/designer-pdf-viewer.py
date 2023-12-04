arr = [int(p) for p in input().split()]
string = input().strip()
strLen = len(string)

maxim = -1
for i in string:
    i = ord(i) - 97 # ord('a') = 97
    if maxim < arr[i]:
        maxim = arr[i]
print(maxim*strLen)
