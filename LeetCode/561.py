class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = sorted(nums)
        sum = 0
        for e in xrange(0, len(numbers), 2):
            n  = numbers[e]
            sum = sum + n
        return sum

if __name__ == "__main__":

    s = Solution()
    numbers = [1,4,3,2]
    print s.arrayPairSum(numbers)