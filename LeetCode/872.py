# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.lnodes = []
        self.leafinorder(root1)
        nodes1 = self.lnodes

        del self.lnodes

        self.lnodes = []
        self.leafinorder(root2)
        nodes2 = self.lnodes

        if nodes1 == nodes2:
            return True
        return False

    def leafinorder(self, root):
        if root:
            self.leafinorder(root.left)
            if root.left == None and root.right == None:
                self.lnodes.append(root.val)
            self.leafinorder(root.right)

if __name__ == "__main__":

    s = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)
    root2.right.left = TreeNode(9)
    root2.right.right = TreeNode(8)

    s.leafSimilar(root1, root2)


