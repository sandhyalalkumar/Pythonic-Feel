class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for a in A:
            B.append(a[::-1])

        #print B
        for i in xrange(0, len(B)):
            for j in xrange(0, len(B[i])):
                if B[i][j] == 1:
                    B[i][j] = 0
                else:
                    B[i][j] = 1

        return B


if __name__ == "__main__":

    A = [[1,1,0],[1,0,1],[0,0,0]]
    #print A
    s = Solution()
    print s.flipAndInvertImage(A)