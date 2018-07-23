from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = deque()
        q.append(root)
        q.append("M")

        sum = 0
        c = 0
        results = []
        while len(q) > 1:
            temp = q.popleft()
            if temp <> "M":
                sum = sum + temp.val
                c = c + 1
            if temp == "M":
                q.append("M")
                avg = round(float(sum)/c, 5)
                results.append(avg)
                sum = 0
                c = 0
            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        avg = round(float(sum)/c, 5)
        results.append(avg)
        return results

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print root.val,
            self.inorder(root.right)

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(10)
    root.left = TreeNode(27)
    root.right = TreeNode(30)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(18)
    root.right.left = TreeNode(23)
    root.right.right = TreeNode(40)

    print s.averageOfLevels(root)





