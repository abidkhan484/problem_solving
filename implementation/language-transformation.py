#!/home/polymath/.pyenv/shims/python

brackets = {'ebong': '&&', 'othoba': '||'}

def getString(a):
  output = ''
  j = 0; i = 0
  length = len(a)
  while (i < length):
    if a[i].isalpha():
      word = ''
      for p in range(i, length):
        if not a[p].isalpha():
          break
        word += a[p]
      output += brackets[word] if (j%2) else word
      i = p if p!=length-1 else p+1
      j += 1
    else:
      output += a[i]
      i += 1
  return output

p = [
  "a othoba b",
  "b ebong c othoba d",
  "ebong ebong othoba othoba ebong",
  "((ebong) othoba ebong) ebong othoba",
  "(ebong othoba (ebong ebong ((othoba)othoba(ebong))))",
  "ebong",
]

for i in p:
  print(getString(i))
