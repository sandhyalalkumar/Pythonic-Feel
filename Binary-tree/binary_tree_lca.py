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

def lowest_common_ancestor(root, n1, n2):
    if root is None:
        return None
    if root.data == n1:
        return root
    if root.data == n2:
        return root

    llca = lowest_common_ancestor(root.left, n1, n2)
    rlca = lowest_common_ancestor(root.right, n1, n2)

    if llca and rlca:
        return root

    if llca and not rlca:
        return llca
    if not llca and rlca:
        return rlca

if __name__ == "__main__":

    root = TreeNode(10, None, None)
    insert(root, TreeNode(11, None, None))
    insert(root, TreeNode(12, None, None))
    insert(root, TreeNode(13, None, None))
    insert(root, TreeNode(14, None, None))
    insert(root, TreeNode(15, None, None))
    insert(root, TreeNode(16, None, None))
    insert(root, TreeNode(17, None, None))
    insert(root, TreeNode(18, None, None))
    insert(root, TreeNode(19, None, None))
    insert(root, TreeNode(20, None, None))

    inorder(root)

    lca = lowest_common_ancestor(root, 13, 16)

    print
    print lca.data

    lca1 = lowest_common_ancestor(root, 17, 20)
    print lca1.data
