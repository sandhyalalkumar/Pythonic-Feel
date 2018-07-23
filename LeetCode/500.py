class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        s1 = set(row1)
        s2 = set(row2)
        s3 = set(row3)

        result = []
        for word in words:
            w = set(word)
            if w.issubset(s1) or w.issubset(s2) or w.issubset(s3):
                result.append(word)
        return result

if __name__ == "__main__":

    s = Solution()
    print s.findWords(["Dad", "Alaska"])
