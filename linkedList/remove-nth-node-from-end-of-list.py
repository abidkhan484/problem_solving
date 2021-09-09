#! /home/polymath/.pyenv/shims/python

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insertInLinkedList(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(val=val)
        if not head:
            return node
        tmp = head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node
        return head

    def removeNthElement(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n = n - 1
        if not n:
            return head.next
        finalList = head
        while n:
            prev = head
            head = head.next
            n = n - 1
        prev.next = head.next
        return finalList


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        
        n = count - n + 1
        head = self.removeNthElement(head, n)
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
        # self.printLinkedList(head)
        head = self.removeNthFromEnd(head, 5)
        self.printLinkedList(head)

s = Solution()
# s.main()
