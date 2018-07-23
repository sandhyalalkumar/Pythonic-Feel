class Polygon:
    def __init__(self, sides):
        self.n = sides

    def sides(self):
        return range(self.n)

    def nodes(self):
        return [(e, e+1) for e in range(self.n)]


class Tringle(Polygon):
    def __init__(self, n, height, base):
        Polygon.__init__(self, n)
        self.height = height
        self.base = base

    def findArea(self):
        return 0.5 * self.height * self.base

if __name__ == "__main__":

    t = Tringle(3, 10, 5)
    print t.findArea()
    print t.sides()
    print t.nodes()