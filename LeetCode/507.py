class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 0
        for i in xrange(1, num):
            if num % i == 0:
                sum = sum + i
        if sum == num:
            return True
        else:
            return False

if __name__ == "__main__":

    s = Solution()
    num = 28
    print s.checkPerfectNumber(num)