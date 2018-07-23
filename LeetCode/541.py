class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        L = len(s)
        results = ""
        c = 0
        for i in xrange(0, L, k):
            if c % 2 == 0:
                results = results + s[i:i+k][::-1]
            else:
                results = results + s[i:i+k]
            c = c + 1
        return results

if __name__ == "__main__":

    s = Solution()
    s1 = "helloworld"
    k = 2
    print s.reverseStr(s1, k)