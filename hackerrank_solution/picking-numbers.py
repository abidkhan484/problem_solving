n = int(input().strip())
arr = [0] * 100

for i in input().split():
    i = int(i)
    arr[i] += 1

temp = arr[0] + arr[1]; maxim = temp
for i in range(1, 99):
    temp = arr[i+1] + temp - arr[i-1]
    if maxim < temp:
        maxim = temp

print(maxim)
