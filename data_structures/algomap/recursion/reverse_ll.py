"""
reversing a linked list with recursion
T: O(n)
S: O(n)
"""

class SinglyNode:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

#print(Head)

def reverse(node: SinglyNode) -> None:
    #base case
    if not node:
        return
    
    reverse(node.next)
    print(node)

reverse(Head)