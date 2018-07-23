class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        b = []
        L = len(numbers)
        for i in xrange(0, L):
            if target - numbers[i] > 0:
                b.insert(target - numbers[i], 1)
        for e in xrange():
            pass


if __name__ == "__main__":

    s = Solution()
    numbers = [1, 2, 3, 5, 10, 11]
    print s.twoSum(numbers, 7)