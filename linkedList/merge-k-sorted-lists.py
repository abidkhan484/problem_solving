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

    def mergeKLists(self, lists: list) -> Optional[ListNode]:
        if not lists:
            return None

        finalHead = ListNode()
        head = finalHead

        p = len(lists); mapping = [0] * p
        i = -10**4
        while i <= 10**4:
            for m in range(p):
                if mapping[m]:
                    continue
                while lists[m] and lists[m].val == i:
                    head.next = lists[m]
                    lists[m] = lists[m].next
                    head = head.next
                if not lists[m]:
                    mapping[m] = 1

            if all(mapping):
                break
            i += 1

        return finalHead.next


    def printLinkedList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val)
            head = head.next

    def getTheLists(self):
        return [[1], [1,2]]


    def main(self):
        a = self.getTheLists()
        lists = []
        for items in a:
            head = ListNode()
            finalHead = head
            for item in items:
                head = self.insertInLinkedList(head, val=item)
            lists.append(finalHead.next)
        head = self.mergeKLists(lists=lists)
        self.printLinkedList(head)

s = Solution()
s.main()

