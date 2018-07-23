def calc_S1(points, counts):
    L_acc = [sum([(2 * i - counts[x] + 1) * y for i, y in enumerate(ps)])
             for x, ps in enumerate(points)]
    S = L_acc[0] * (counts[1] + 2 * counts[2]) + L_acc[2] * (counts[1] + 2 * counts[0]) + L_acc[1] * (counts[0] + counts[2])
    return S


def solve(N, points):
    points1 = [[] for _ in xrange(3)]
    for x, y in points:
        points1[x - 1].append(y)
    points = [sorted(ps) for ps in points1]
    counts = [len(p) for p in points]

    S1 = calc_S1(points, counts)

    sums_y2 = [[0] * (counts[1] + 1), [sum(points[1])] + [0] * counts[1]]
    for i in xrange(counts[1]):
        sums_y2[0][i + 1] = sums_y2[0][i] + points[1][i]
        sums_y2[1][i + 1] = sums_y2[1][i] - points[1][i]

    S2 = 0
    J0 = 0
    if counts[0] == 0 or counts[1] == 0 or counts[2] == 0:
        return 0.5 * (S1 + S2)

    for y1 in points[0]:
        yy = y1 + points[2][0]
        while J0 < counts[1] and 2 * points[1][J0] < yy:
            J0 += 1
        J1 = J0
        for y3 in points[2]:
            yy = y1 + y3
            while J1 < counts[1] and 2 * points[1][J1] < yy:
                J1 += 1
            YJ = sums_y2[1][J1] - sums_y2[0][J1]
            S2 += 2 * YJ + (2 * J1 - counts[1]) * yy

    return 0.5 * (S1 + S2)


T = int(raw_input())

for tc in xrange(1, T + 1):
    N = int(raw_input())
    points = [map(int, raw_input().rstrip().split(' ')) for _ in xrange(N)]
    print points
    s1 = solve(N, points)
    print "%.2f" % s1