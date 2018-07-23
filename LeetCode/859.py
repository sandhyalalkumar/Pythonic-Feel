from collections import Counter

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        LA = len(A)
        LB = len(B)

        if A == B:
            if A == "":
                return True
            a = Counter(A)
            if a.most_common(1)[0][1] >= 2:
                return True

        if LA <> LB:
            return False

        r = []
        for i in xrange(0, LA):
            if ord(A[i]) - ord(B[i]) <> 0:
                r.append(ord(A[i]) - ord(B[i]))
        if len(r) <> 2:
            return False
        else:
            if r[0] == -r[1]:
                return True
        return False

if __name__ == "__main__":

    s = Solution()
    A = "aa"
    B = "aa"
    print s.buddyStrings(A, B)
