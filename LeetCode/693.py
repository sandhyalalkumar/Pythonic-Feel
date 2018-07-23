class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a1 = 0
        b1 = 0

        while n:
            a1 = n & 1
            n = n >> 1
            b1 = n & 1
            if a1 == b1:
                return False
        return True

if __name__ == "__main__":

    s = Solution()
    n = 3
    print s.hasAlternatingBits(n)