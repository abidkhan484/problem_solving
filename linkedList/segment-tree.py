from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class SegmentTree:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(self.nums)
        self.head = self.makeSegmentTree(0, self.length - 1)

    def makeSegmentTree(self, left, right):
        if left == right:
            return Node(self.nums[left])

        mid = (left + right) // 2
        leftNode = self.makeSegmentTree(left, mid)
        rightNode = self.makeSegmentTree(mid+1, right)

        head = Node(leftNode.value + rightNode.value)
        head.left = leftNode
        head.right = rightNode
        return head

SegmentTree([7,2,7,2,0])
