class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        L = len(s)
        results = ""
        for i in xrange(0, L):
            if s[i] in ["a", "e", "i", "o", "u"]:
                vowels.append(s[i])

        for j in xrange(0, L):
            if s[j] in ["a", "e", "i", "o", "u"]:
                results = results + vowels.pop()
            else:
                results = results + s[j]
        return results

if __name__ == "__main__":

    s = Solution()
    word = "hey man this is sandhyalal"
    word = "hello"
    print s.reverseVowels(word)