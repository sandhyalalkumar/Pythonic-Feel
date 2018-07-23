import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        D = []
        for i in xrange(1, int(math.sqrt(num)+1)):
            if num % i == 0:
                D.append(num / i)
        E = []
        for e in D:
            if num / e <> e:
                E.append(num / e)
        F = D + E

        if sum(F[1:]) == num:
            return True
        return False


if __name__ == "__main__":

    s = Solution()
    num = 28
    s.checkPerfectNumber(num)