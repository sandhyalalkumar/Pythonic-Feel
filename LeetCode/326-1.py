import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # print math.log10(n) % math.log10(3)
        if math.log10(n) % math.log10(3) == 0:
            return True

        return False


if __name__ == "__main__":

    s = Solution()
    print s.isPowerOfThree(81)