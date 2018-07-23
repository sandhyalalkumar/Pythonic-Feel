class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
        return zip(*A)

if __name__ == "__main__":

    s = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A =  [[1,2,3],[4,5,6]]

    print s.transpose(A)