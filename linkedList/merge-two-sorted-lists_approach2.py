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

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: 
            return l2
        if not l2: 
            return l1
        finalHead = ListNode()
        head = finalHead
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        head.next = l1 if l1 else l2

        return finalHead.next


    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next


    def main(self):
        arr = [1,2,3,4,5]
        arr2 = [1,1,3,4,6]
        [head, head2] = [None, None]
        for val in arr:
            head = self.insertInLinkedList(head, val)

        for val in arr2:
            head2 = self.insertInLinkedList(head2, val)

        head = self.mergeTwoLists(head, head2)
        self.printLinkedList(head)

s = Solution()
s.main()

