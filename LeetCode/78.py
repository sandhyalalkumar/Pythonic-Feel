class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = len(nums)
        subsets = []
        for i in xrange(0, 2 ** L):
            j = i
            C = L - 1
            subset = []
            while j:
                flag = j & 1
                if flag == 1:
                    subset.append(nums[C])
                C = C - 1
                j = j >> 1
            subsets.append(subset)
        return subsets


if __name__ == "__main__":

    s = Solution()
    L = [1,2,3]
    print s.subsets(L)