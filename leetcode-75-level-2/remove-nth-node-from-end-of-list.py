
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        n = length - n
        if not n:
            return head.next
        prev = head
        curr = head
        while n:
            prev = curr
            curr = curr.next
            n -= 1
        prev.next = curr.next
        return head
