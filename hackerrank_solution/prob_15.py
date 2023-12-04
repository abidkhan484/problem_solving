class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        current = head
        if head is None:
            head = Node(data)
        else:
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return head

    def ReversePrint(self, head):
        if head:
            Solution.ReversePrint(self, head.next)
            print(head.data, end=' ')


    def InsertNth(self, head, data, position):
        start = head
        if position==0:
            return Node(data, head)
        while position > 1:
            head = head.next
            position -= 1
        head.next = Node(data, head.next)
        return start

    def Delete(self, head, position):
        if position == 0:
            return head.next

        start = head
        while position > 1:
            prev = head
            head = head.next
            position -= 1
        prev.next = head.next
        return start


   
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)

print()

mylist.ReversePrint(head)
