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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        finalHead = ListNode(head.next.val)
        prev = None
        while head and head.next:
            val = head.next.val
            head.next = head.next.next
            if prev:
                newNode = ListNode(val)
                prev.next = newNode
            else:
                newNode = finalHead
            prev = head
            newNode.next = head
            head = head.next

        return finalHead
    
    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next


    def main(self):
        arr = [1,2,3]
        head = None
        for val in arr:
            head = self.insertInLinkedList(head, val)
        # self.printLinkedList(head)
        head = self.swapPairs(head)
        self.printLinkedList(head)

s = Solution()
# s.main()