class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        base3 = self.baseconvert(n, 3)
        tostr = str(base3)
        L = len(tostr)
        zeros = 0
        for i in tostr:
            if i == "0":
                zeros = zeros + 1

        if tostr[0] == "1" and zeros == L - 1:
            return True
        return False

    def baseconvert(self, n, base):
        """convert positive decimal integer n to equivalent in another base (2-36)"""

        digits = "0123456789abcdefghijklmnopqrstuvwxyz"

        try:
            n = int(n)
            base = int(base)
        except:
            return ""

        if n < 0 or base < 2 or base > 36:
            return ""

        s = ""
        while 1:
            r = n % base
            s = digits[r] + s
            n = n / base
            if n == 0:
                break

        return s

if __name__ == "__main__":

    s = Solution()
    print s.baseconvert(-27, 3)
    print s.isPowerOfThree(81)