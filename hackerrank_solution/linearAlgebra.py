# i can make it better
# but now it can do what i want for my solving

def matrixMul(p, q):

    l = len(p); le = len(q)
    s = [[] for _ in range(l)]
    for i in range(l):
            for j in range(le):
                    total = 0
                    for k in range(le):
                            total += p[i][k] * q[k][j]
                    s[i].append(total)
    return s

a, b = map(int, input().split())
p = [[int(x) for x in input().split()] for _ in range(a)]
q = [[int(p) for p in input().split()] for _ in range(b)]

s = matrixMul(p, q)
print(s)
s = matrixMul(s, s)
print(s)
s = matrixMul(s, s)
print(s)
