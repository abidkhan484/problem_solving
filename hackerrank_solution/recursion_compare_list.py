def compare_list(p, q):
    if len(p) != len(q):
        return 0
    if len(p) == len(q) == 0:
        return 1
    
    if p[0] != q[0]:
        print(p[0], q[0], end=' ')
        print()
        return 0
    
    return compare_list(p[1:], q[1:])

p = [1, 2, 3]
q = [1, 2, 3, 4]

print(compare_list(p, q))
