# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None:
            return False

        hashset = set()

        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            v = k - temp.val
            print v
            if temp.val in hashset:
                return True
            else:
                hashset.add(v)

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        return False

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(7)

    # k = 14
    # print s.findTarget(root, k)

    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(7)

    k = 9
    print s.findTarget(root1, k)
