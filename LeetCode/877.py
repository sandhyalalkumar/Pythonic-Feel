class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        Alex = 0
        Lee = 0
        while piles:
            if piles[0] > piles[-1]:
                Alex = Alex + piles[0]
                del piles[0]
            else:
                Alex = Alex + piles[-1]
                del piles[-1]

            if piles[0] > piles[-1]:
                Lee = Lee + piles[0]
                del piles[0]
            else:
                Lee = Lee + piles[-1]
                del piles[-1]

            if Alex > Lee:
                return True

        return False

if __name__ == "__main__":

    s = Solution()
    stones = [5,3,4,5, 10, 10]
    stones = [3,2,10,4]
    print s.stoneGame(stones)