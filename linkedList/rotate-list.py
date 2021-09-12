#! /home/polymath/.pyenv/shims/python

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def lengthOfTheLinkedList(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = self.lengthOfTheLinkedList(head)
        n = k % length
        if not n:
            return head

        i = length - n - 1
        curhead = head
        while i:
            curhead = curhead.next
            i -= 1
        backHead = head
        finalHead = curhead.next
        curhead.next = None
        curhead = finalHead
        while curhead.next:
            curhead = curhead.next
        curhead.next = backHead
        # self.printLinkedList(finalHead)

        return finalHead
    
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
        head = None
        for val in arr:
            head = self.insertInLinkedList(head, val)
        head = self.rotateRight(head, 2)
        self.printLinkedList(head)

s = Solution()
s.main()

