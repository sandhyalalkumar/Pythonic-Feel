class Solution(object):
    def DividingNumber(self, num):
        n = str(num)
        if "0" in n:
            return False

        N = num
        while N > 10:
            r = N % 10
            N = N / 10
            if num % r <> 0:
                return False
        if num % N <> 0:
            return False
        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []
        for e in xrange(left, right+1):
            if self.DividingNumber(e):
                numbers.append(e)
        return numbers

if __name__ == "__main__":

    s = Solution()
    left = 1
    right = 22
    print s.selfDividingNumbers(left, right)

    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 21, 22]