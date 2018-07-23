from collections import Counter
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        L = len(candies)
        C = Counter(candies)
        if L/2 == len(C):
            return L/2
        if len(C) > L/2:
            return L/2
        if len(C) < L/2:
            return len(C)

if __name__ == "__main__":

    s = Solution()
    A = [1,1,2,3,5,6]
    A = [1,1,1,1,2,2,3,3,4,4]
    print s.distributeCandies(A)