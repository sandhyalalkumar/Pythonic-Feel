from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # !?',;.
        words = paragraph.replace("!", "")
        words1 = words.replace("?", "")
        words2 = words1.replace("'", "")
        words3 = words2.replace(",", "")
        words4 = words3.replace(";", "")
        words5 = words4.replace(".", "")

        words6 = words5.lower().split()
        words7 = []
        counter = Counter(words6)
        for w in banned:
            counter[w] = 0

        return counter.most_common(1)[0][0]

if __name__ == "__main__":

    s = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print s.mostCommonWord(paragraph, banned)