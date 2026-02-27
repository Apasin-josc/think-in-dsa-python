class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    

A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(7)
D = TreeNode(1)
E = TreeNode(3)
F = TreeNode(6)
G = TreeNode(9)

#[4, 2, 7, 1, 3, 6, 9]
#[4, 7, 2, 9, 6, 3, 1]


A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G

def invert_binary_tree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    print(root.val)
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    
    return root
    

invert_binary_tree(A)
