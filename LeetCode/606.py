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
s = ""
def preorder(root):
    if root:
        global s
        s += "("
        s += str(root.data)
        preorder(root.left)
        preorder(root.right)
        s += ")"

if __name__ == "__main__":

    # root = TreeNode(1, None, None)
    # root.left = TreeNode(2, None, None)
    # root.left.left = TreeNode(4, None, None)
    # root.right = TreeNode(3, None, None)
    # inorder(root)
    # print
    # preorder(root)
    # print s


    root1 = TreeNode(1, None, None)
    root1.left = TreeNode(2, None, None)
    root1.left.right = TreeNode(4, None, None)
    root1.right = TreeNode(3, None, None)

    preorder(root1)
    print s