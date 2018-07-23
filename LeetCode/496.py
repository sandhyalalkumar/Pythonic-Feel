class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        L = len(nums)
        for e in findNums:
            ind = nums.index(e)
            if ind == L - 1:
                results.append(-1)
                continue
            flag = False
            for i in xrange(ind+1, L):
                if nums[i] > e:
                    results.append(nums[i])
                    flag = True
                    break
            if flag == False:
                results.append(-1)

        return results

if __name__ == "__main__":

    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]

    print s.nextGreaterElement(nums1, nums2)