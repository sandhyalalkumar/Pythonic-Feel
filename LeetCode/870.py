from itertools import izip
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        print sorted(A)
        print sorted(B)
        d = dict(izip(sorted(B), sorted(A)))

        A = []
        for e in B:
            A.append(d[e])
        return A


if __name__ == "__main__":

    s = Solution()
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    A=[12, 24, 8, 32]
    B=[13, 25, 32, 11]
    print s.advantageCount(A, B)


