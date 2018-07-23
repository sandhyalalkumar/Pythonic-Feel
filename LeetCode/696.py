class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        for i in xrange(0, L):
            pass



if __name__ == "__main__":

    s = Solution()
    word = "00110011"
    s.countBinarySubstrings(word)