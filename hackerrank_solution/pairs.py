n, k = map(int, input().split())
arr = [int(p) for p in input().split()]

arr.sort(); j=1; count=0
for i in range(n):

    if arr[i] + k > arr[-1]:
        break

    while (j < n):
        if arr[j] > arr[i]+k:
            break
        if arr[j]==arr[i]+k:
            count += 1
        j += 1

    j -= 1
    
print(count)


'''
#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value

    answer = 0
    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))

'''
