class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ll = len(A)
        AA = False
        BB = False
        ind = 0
        for i in xrange(0, ll-1):
            if A[i] < A[i+1]:
                AA = True
                ind = i + 1
            else:
                break

        for j in xrange(ind, ll-1):
            if A[j] > A[j+1]:
                BB = True
            else:
                BB = False
                break

        if AA and BB:
            return ind
        return 0

if __name__ == "__main__":

    s = Solution()
    A = [3,2,1]
    A = [3,4,5,1]
    print s.peakIndexInMountainArray(A)