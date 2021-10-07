#! /home/polymath/.pyenv/shims/python

def binarySearch(key, arr):
    length = len(arr)
    left, right = 0, length-1
    arr.sort()

    while (left < right):
        mid = left + (right-left) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [ 2, 3, 4, 10, 40 ]
key = 40
print(binarySearch(key, arr))
