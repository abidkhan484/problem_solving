right=10**6; left=-1; down=-1; up=10**6
rightUpCorner=10**6; leftUpCorner=10**6;
rightDownCorner=-1; leftDownCorner=-1

n, k = map(int, input().split())
qrow, qcol = map(int, input().split())

for _ in range(k):

    r, c = map(int, input().split())

    if qrow == r:
        if c > qcol and c < right:
            right = c
        elif c < qcol and c > left:
            left = c
    elif qcol == c:
        if r > qrow and r < up:
            up = r
        elif r < qrow and r > down:
            down = r
    elif abs(qrow-r) == abs(qcol-c):
        if r > qrow and c < qcol and leftUpCorner > r:
            leftUpCorner = r
        if r < qrow and c > qcol and rightDownCorner < r:
            rightDownCorner = r
        if r > qrow and c > qcol and rightUpCorner > r:
            rightUpCorner = r
        if r < qrow and c < qcol and leftDownCorner < r:
            leftDownCorner = r


total = 0
if left != -1:
    total += qcol-left-1
else:
    total += qcol-1
print(total, 'left')

if right != 10**6:
    total += right-qcol-1
else:
    total += (n-qcol)
print(total, 'right')

if down != -1:
    total += qrow-down-1
else:
    total += qrow-1
print(total, 'down')

if up != 10**6:
    total += (up-qrow-1)
else:
    total += (n-qrow)
print(total, 'up')

if rightUpCorner != 10**6:
    total += (rightUpCorner-qrow-1)
else:
    total += min(n-qcol, n-qrow)
print(total, 'rightUp')

if rightDownCorner != -1:
    total += (qrow-rightDownCorner-1)
else:
    total += min((n-qcol), (qrow-1))
print(total, 'rightDown')

if leftUpCorner != 10**6:
    total += (leftUpCorner-qrow-1)
else:
    total += min((qcol-1), (qrow-1))
print(total, 'leftUP')

if leftDownCorner != -1:
    total += (qrow-leftDownCorner-1)
else:
    total += min(n-qrow, qcol-1)
print(total, 'leftDown')
