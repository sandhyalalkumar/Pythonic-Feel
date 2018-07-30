from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        s = (L * (L + 1)) / 2

        rs = sum(nums)

        d = Counter(nums)
        ans = []
        for e in nums:
            if d[e] == 2:
                if rs < s:
                    return [e, e+1]
                else:
                    return [e, e-1]
        return ans

if __name__ == "__main__":

    s = Solution()
    L = [2, 2]
    print s.findErrorNums(L)
