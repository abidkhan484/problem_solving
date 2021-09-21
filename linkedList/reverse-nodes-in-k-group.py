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
        head = self.reverseKGroup(head, 3)
        self.printLinkedList(head)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        head = ListNode()
        finalHead = head
        i = -1; length = len(li)

        while True:
            j = i
            i += k
            if i >= length:
                break
            for p in range(i,j,-1):
                head.next = ListNode(li[p])
                head = head.next
        for p in range(j+1,length):
            head.next = ListNode(li[p])
            head = head.next
        return finalHead.next

            
        
s = Solution()
s.main()