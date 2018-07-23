from itertools import izip

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        mapping = dict(izip(letters, widths))
        lc = 0
        c = 1
        i = 0
        strlen = len(S)

        while i < strlen:
            if lc + mapping[S[i]] > 100:
                lc = 0
                c =  c + 1
            else:
                lc = lc + mapping[S[i]]
                i = i + 1
        return [c, lc]

if __name__ == "__main__":

    s = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print s.numberOfLines(widths, S)

    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print s.numberOfLines(widths, S)