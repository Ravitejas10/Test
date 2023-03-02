class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        preorder(root.right)
        print(root.val)

root=Node(1)
root.left=Node(2)
root.right=Node(3)

inorder(root)
print("*"*50)
preorder(root)
print("*"*50)
postorder(root)