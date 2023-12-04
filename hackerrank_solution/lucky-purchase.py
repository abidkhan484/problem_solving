laptop = -1
minPrice = 10**9+1
for _ in range(int(input().strip())):
    name, lapPrice = input().split()
    if ('4' not in lapPrice) or ('7' not in lapPrice):
        continue
    fours = lapPrice.count('4')
    sevens = lapPrice.count('7')
    if (fours != sevens) or (len(lapPrice) > (fours+sevens)):
        continue
    lapPrice = int(lapPrice)
    if lapPrice < minPrice:
        laptop = name

print(laptop)
