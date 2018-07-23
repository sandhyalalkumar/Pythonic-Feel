class Solution(object):
    c1 = ""
    c2 = ""
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        i = 0
        j = L - 1
        S = list(s)
        while i < j:
            while i < j:
                if S[i] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                    i = i + 1
                else:
                    self.c1 = S[i]
                    break

            while i < j:
                if S[j] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                    j = j - 1
                else:
                    self.c2 = S[j]
                    break
            a = S[i]
            S[i] = S[j]
            S[j] = a
            i = i + 1
            j = j - 1
        return "".join(S)

if __name__ == "__main__":

    s = Solution()
    word = "hell othis"
    print len(word)
    S = s.reverseVowels(word)
    print S
    print len(S)
    print "".join(S)