class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if node.data > root.data:
        if root.right == None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print root.data
        inorder(root.right)