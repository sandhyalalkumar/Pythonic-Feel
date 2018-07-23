class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hourleds = 4
        minuteleds = 6
        for i in xrange(4, -1, -1):
            print i, 4 - i
        



if __name__ == "__main__":

    s = Solution()
    num = 10
    s.readBinaryWatch(num)