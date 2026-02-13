```
class SinglyNode:
    def __init__(self, val, next =None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    
    # Display Linked List - O(n)
    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(elements))
    
    # Search for a node val - O(n)
    def search(head, val):
        curr = head
        while curr:
            if val == curr.val:
                return True
            curr = curr.next
        
        return False

head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
head.next = A
A.next = B
B.next = C
#print(head)

print(SinglyNode.display(head))
print(SinglyNode.search(head,2))
```
