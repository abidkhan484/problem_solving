#insert head of a linked list
def Insert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

#insert tail of a linked list
def insert(self,head,data): 
    current = head
    if head is None:
        head = Node(data)
    else:
        while (current.next != None):
            current = current.next
        current.next = Node(data)
    return head


#insertNth position of a linked list
def InsertNth(head, new_data, position):
    if position is 0:
        new_node = Node(data)
        
        new_node.next = head
        head = new_node
        return head
    else:
        current = head
        while (position-1):
            current = current.next
            position -= 1
        temp = current.next
        current.next = Node(data)
        current = current.next
        current.next = temp
        head = current.next
        return head


head = None 
insert(head, 2)
insert(head, 3)
insert(head, 5)
insert(head, 4)



insertNth(head, 9, 2)
