class Solution(object):
    def reverseWords(self, str):
        """
        :type str: str
        :rtype: int
        """
        nstr = str.split(" ")
        rstr = []
        for s in nstr:
            rstr.append(s[::-1])
        return " ".join(rstr)

if __name__ == "__main__":

    s = Solution()
    print s.myAtoi("hello this is sandy")