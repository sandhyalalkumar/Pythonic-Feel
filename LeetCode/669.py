# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None

        newroot = None
        if root.val >= L and root.val <= R:
            newroot = TreeNode(root.val)


        def levelorder(root):
            q1 = deque()
            q1.append(root)

            while q1:
                temp = q1.popleft()
                if L <= temp.val <= R:
                    pass

                if root.left:
                    q1.append(temp.left)
                if root.right:
                    q1.append(temp.right)

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
    
if __name__ == "__main__":

    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(10)
    root.right.right  = TreeNode(12)

    s.trimBST(root, 7, 10)


