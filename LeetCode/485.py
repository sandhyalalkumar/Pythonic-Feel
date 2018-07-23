class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L = len(nums)
        if sum(nums) == L:
            return L
        if sum(nums) == 1:
            return 1

        c = 0
        max = 0
        for e in nums:
            if e == 1:
                c = c + 1
            else:
                if e == 0:
                    if max < c:
                        max = c
                        c = 0
        if nums[-1] == 1:
            if max > c:
                return max
            else:
                return c
        return max


if __name__ == "__main__":

     s = Solution()
     word = [0,0,1,1,1,0,1,1]
     print s.findMaxConsecutiveOnes(word)