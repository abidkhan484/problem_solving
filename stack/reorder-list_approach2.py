#! /home/polymath/.pyenv/shims/python

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insertInLinkedList(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(val=val)
        if not head:
            return node
        tmp = head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node
        return head

    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next


    def main(self):
        arr = [1,2,3,4,5]
        for val in arr:
            self.head = self.insertInLinkedList(self.head, val)
        # self.printLinkedList(head)
        self.reorderList(self.head)
        self.printLinkedList(self.head)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nhead = head.next
        li = []
        while nhead:
            li.append(nhead)
            nhead = nhead.next

        nhead = head
        length = len(li)
        iterLen = length // 2
        for i in range(iterLen):
            li[length-i-1].next = None
            nhead.next = li[length-i-1]
            nhead = nhead.next

            li[i].next = None
            nhead.next = li[i]
            nhead = nhead.next

        if length&1:
            li[iterLen].next = None
            nhead.next = li[iterLen]

        # self.printLinkedList(head)
        

s = Solution()
s.main()