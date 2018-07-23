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

def inorder(root):
    if root:
        inorder(root.left)
        print root.data,
        inorder(root.right)

def findpath(root, data, path):
    if root is None:
        return False

    path.append(root.data)

    if root.data == data:
        return True

    if((root.left <> None and findpath(root.left, data, path)) or (root.right <> None and findpath(root.right, data, path))):
        return True
    path.pop()
    return False

if __name__ == "__main__":

    root = TreeNode(10, None, None)
    insert(root, TreeNode(15, None, None))
    insert(root, TreeNode(5, None, None))
    insert(root, TreeNode(25, None, None))
    insert(root, TreeNode(35, None, None))
    insert(root, TreeNode(67, None, None))

    inorder(root)

    path1 = []
    findpath(root, 5, path1)
    path2 = []
    findpath(root, 67, path2)

    print path1
    print path2