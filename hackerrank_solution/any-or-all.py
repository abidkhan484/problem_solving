n = int(input().strip())
li = [p for p in input().split()]
print(all([int(p)>0 for p in li]) and any(p==p[::-1] for p in li))
