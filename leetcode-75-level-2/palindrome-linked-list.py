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

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        curr = head.next
        head.next = None
        prev = head

        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev

        return curr

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        isPalin = 1
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return isPalin

        half_length = length // 2 if length & 1 else (length // 2)-1
        left = head
        curr = head
        prev = head
        while half_length:
            prev = curr
            curr = curr.next
            half_length -= 1
        right = curr.next
        if length&1:
            prev.next = None
        else:
            curr.next = None

        reversed_right = self.reverseLinkedList(right)
        while left:
            if left.val != reversed_right.val:
                isPalin = 0
                break
            left, reversed_right = left.next, reversed_right.next

        return isPalin

    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next

    def main(self):
        arr = [1,2,3,2,1]
        arr = [1,1]
        head = None
        for val in arr:
            head = self.insertInLinkedList(head, val)
        # self.printLinkedList(head)
        head = self.reverseLinkedList(head)
        # self.printLinkedList(head)
        print(self.isPalindrome(head))

s = Solution()
s.main()
