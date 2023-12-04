import re

n = int(input().strip())
sentences = [input() for _ in range(n)]

q = int(input().strip())
query = [input() for _ in range(q)]

for i in range(n):
    for j in range(q):
        

R = r'\w'+query+'\w'

