class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for num in xrange(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                results.append("FizzBuzz")
            elif num % 3 == 0:
                results.append("Fizz")
            elif num % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(num))
        return results

if __name__ == "__main__":

    s = Solution()
    n = 30
    print s.fizzBuzz(n)