class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
   
        strlen = len(S)
        eindex = []
        for i in xrange(0, strlen):
            if S[i] == C:
                eindex.append(i)
        mindistance = []
        for i in xrange(0, strlen):
            lmin = []
            for j in eindex:
                lmin.append(abs(i-j))
            mindistance.append(min(lmin))
        return mindistance

if __name__ == "__main__":

    s = Solution()
    S = "loveleetcode"
    C = 'e'
    print s.shortestToChar(S, C)