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

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd, even = ListNode(0), ListNode(0)
        odd_iter, even_iter = odd, even
        while head and head.next:
            odd_iter.next = ListNode(head.val)
            even_iter.next = ListNode(head.next.val) if head.next else None

            head, odd_iter, even_iter = head.next.next, odd_iter.next, even_iter.next

        if head:
            odd_iter.next = head
            odd_iter = odd_iter.next

        odd_iter.next = even.next
        return odd.next

    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next

    def main(self):
        arr = []
        head = None
        for val in arr:
            head = self.insertInLinkedList(head, val)
        # self.printLinkedList(head)
        head = self.oddEvenList(head)
        self.printLinkedList(head)

s = Solution()
s.main()
