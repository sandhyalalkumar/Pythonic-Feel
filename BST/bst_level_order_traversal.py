from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def level_order_traversal(root):
    que = deque()
    que.append(root)

    while que:
        temp = que.popleft()
        print temp.data
        if temp.left:
            que.append(temp.left)
        if temp.right:
            que.append(temp.right)

def inorder(root):
    if root:
        inorder(root.left)
        print root.data
        inorder(root.right)

if __name__ == "__main__":

    root = TreeNode(10)
    insert(root, TreeNode(5))
    insert(root, TreeNode(10))
    insert(root, TreeNode(15))
    insert(root, TreeNode(6))
    insert(root, TreeNode(12))
    insert(root, TreeNode(11))

    # inorder(root)

    level_order_traversal(root)