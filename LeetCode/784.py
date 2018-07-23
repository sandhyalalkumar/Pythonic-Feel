class Solution(object):
    def case_permute(self, S, i, L):
        if i == L:
            print S
        else:
            for j in xrange(i, L+1):
                S = S[:j]+S[j].upper()+S[j+1:]
                self.case_permute(S, j+1, L)
                S = S[:j]+S[j].lower()+S[j+1:]

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = len(S)
        self.case_permute(S, 0, L-1)

if __name__ == "__main__":

    s = Solution()
    word = "sand"
    s.letterCasePermutation(word)