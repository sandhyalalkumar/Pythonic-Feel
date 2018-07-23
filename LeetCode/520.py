class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        L = len(word)
        if L == 1:
            if word[0].isupper():
                return True
            return False

        if L > 1:
            if word.isupper():
                return True
            elif word.islower():
                return True
            elif word[0].isupper() and word[1:].islower():
                return True
        return False

if __name__ == "__main__":

    s = Solution()
    word = "Google"
    word = "A"
    word = "USA"
    word = "Amazon"
    word = "a"
    print s.detectCapitalUse(word)