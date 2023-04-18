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
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = node
        return head

    def mergeList(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        curr.next = left if left else right
        while left and right:
            if left.val <= right.val:
                temp = left
                left = left.next
                curr.next = temp
            else:
                temp = right
                right = right.next
                curr.next = temp
            curr = curr.next
        curr.next = left if left else right
        return head.next

        # head = ListNode(0)
        # curr = head
        # while left and right:
        #     if left.val <= right.val:
        #         curr.next = ListNode(left.val)
        #         left = left.next
        #     else:
        #         curr.next = ListNode(right.val)
        #         right = right.next
        #     curr = curr.next
        # curr.next = left if left else right
        # return head.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeList(left, right)

    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next

    def main(self):
        arr = [4,3,2,1,5]
        head = None
        for val in arr:
            head = self.insertInLinkedList(head, val)
        # self.printLinkedList(head)
        head = self.sortList(head)
        self.printLinkedList(head)

s = Solution()
s.main()
