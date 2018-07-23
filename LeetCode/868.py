class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        cc = 0
        M = N
        while M:
            b1 = M & 1
            if b1 == 1:
                cc = cc + 1
            M = M >> 1
        if cc == 1:
            return 0

        maxgap = 0
        c = 0
        nex = 0
        while N:
            a1 = N & 1
            if a1 == 1:
                prev = nex
                nex = c
                print nex, prev
                if nex - prev > maxgap:
                    maxgap = nex-prev
            c = c + 1
            N = N >> 1
        return maxgap


if __name__ == "__main__":

    s = Solution()
    N = 12
    print s.binaryGap(N)