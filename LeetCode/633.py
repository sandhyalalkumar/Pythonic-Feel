import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        a = 0
        while a * a <= c:
            b = math.sqrt(c-a*a)
            bb  = str(b)
            if bb.split(".")[1] == "0":
                return True
            a =  a + 1
        return False

if __name__ == "__main__":

    s = Solution()
    print s.judgeSquareSum(4)
