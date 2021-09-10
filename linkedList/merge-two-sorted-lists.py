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
        head = None
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            if val1 > val2:
                head = self.insertInLinkedList(head, val2)
                l2 = l2.next
            elif val1 < val2:
                head = self.insertInLinkedList(head, val1)
                l1 = l1.next
            else:
                head = self.insertInLinkedList(head, val1)
                head = self.insertInLinkedList(head, val2)
                l1 = l1.next
                l2 = l2.next
        
        remainValues = l1 if l1 else l2
        while remainValues:
            head = self.insertInLinkedList(head, remainValues.val)
            remainValues = remainValues.next

        return head
        