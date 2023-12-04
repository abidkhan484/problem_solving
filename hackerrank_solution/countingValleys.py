# this problem is not solved yet
# i just can't understand the problem statement

n = int(input().strip())
arr = input().strip()

level=0; count=0
for i in arr:

    if i=='U':
        level += 1
    else:
        level -= 1

    if level > 0:
        count += 1
    print(level)

print(count)
