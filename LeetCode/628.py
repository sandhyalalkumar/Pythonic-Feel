class Solution(object):
    def maximumProduct(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(n)
        L = len(nums)
        return max(nums[0]*nums[1]*nums[L-1], nums[L-1]*nums[L-2]*nums[L-3])


if __name__ == "__main__":

    s = Solution()

    num =   [1,3,7,10,5,-1,-20]

    print s.maximumProduct(num)