```
class DoublyNode:
    def __init__(self, val, next= None, prev= None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)
    
    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' <-> '.join(elements))
        
    def insert_at_beginning(head, tail, val):
        new_node = DoublyNode(val, next=head)
        head.prev = new_node
        return new_node, tail
    
    def insert_at_end(head, tail, val):
        new_node = DoublyNode(val, prev= tail)
        tail.next = new_node
        return head, new_node
    
head = tail = DoublyNode(1)
print(DoublyNode.display(head))
head, tail = DoublyNode.insert_at_beginning(head,tail, 3)
(DoublyNode.display(head))
```
