#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root:
                uniques.add(root.val)
                dfs(root.left)
                dfs(root.right)

        uniques = set()
        dfs(root)
        min, secondmin = root.val, float('inf')
        for v in uniques:
            if min < v < secondmin:
                secondmin = v
        return secondmin if secondmin < float('inf') else -1

if __name__ == "__main__":

    s = Solution()

    root1 = TreeNode(2)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(7)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    print s.findSecondMinimumValue(root1)
