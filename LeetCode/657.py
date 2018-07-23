from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cdict = Counter(moves)
        if cdict["U"] == cdict["D"] and cdict["R"] == cdict["L"]:
            return True
        return False

if __name__ == "__main__":

    s = Solution()
    print s.judgeCircle("RLUDD")

