class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        p = x ^ y

        c =  0
        while p:
            k = p & 1
            if k > 0:
                c = c + 1
            p = p >> 1
        return c

if __name__ == "__main__":

    s = Solution()
    x = 1
    y = 4
    print s.hammingDistance(x, y)