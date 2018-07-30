from itertools import combinations
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(x, y, z):
            return 0.5 * abs( x[0]*y[1]+y[0]*z[1]+z[0]*x[1] - x[0]*z[1]-z[0]*y[1]-y[0]*x[1])

        return max([area(*coordinates) for coordinates in combinations(points, 3)])


if __name__ == "__main__":

    s = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print s.largestTriangleArea(points)