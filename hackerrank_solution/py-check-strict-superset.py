A = set(input().split())
n = int(input().strip())

for _ in range(n):
    B = set(input().split())
    if not (A.issuperset(B)):
        print(False)
        break
else:
    print(True)

# A > B also returns A.issuperset(B)
# two liner:
'''
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input().split()))))
'''
