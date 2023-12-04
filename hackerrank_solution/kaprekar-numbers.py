# this is not what i should do
# karNum is get from wikipedia.
# write the code again

karNum = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272, 7777, 9999, 17344, 22222, 77778, 82656, 95121, 99999]
length = len(karNum)
p = int(input().strip()); q = int(input().strip())

c = 0
for i in range(length):
    if (p <= karNum[i]) and (q >= karNum[i]):
        print(karNum[i], end=' ')
        c += 1
if not c:
    print('INVALID RANGE')
