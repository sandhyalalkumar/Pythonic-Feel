from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, node):
    q = deque()
    q.append(root)

    while len(q) > 0:
        temp = q.popleft()

        if not temp.left:
            temp.left = node
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = node
            break
        else:
            q.append(temp.right)

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)

if __name__ == "__main__":

    root = TreeNode(10, None, None)
    insert(root, TreeNode(11, None, None))
    insert(root, TreeNode(12, None, None))
    insert(root, TreeNode(13, None, None))
    insert(root, TreeNode(14, None, None))
    insert(root, TreeNode(15, None, None))
    insert(root, TreeNode(16, None, None))

    result = []
    inorder(root, result)
    print result

