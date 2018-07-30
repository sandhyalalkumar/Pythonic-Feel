for i in xrange(input()):
    a, b, c, x, y = map(int, raw_input().split())
    if a + b + c < x + y or a + b + c > x + y:
        print "NO"
    else:
        l = sorted([a, b, c])
        q = min(x, y)
        w = max(x, y)
        f = 0

        if abs(l[1] - abs(w - l[2])) + l[0] == q:
            f = 1
            print "YES"
        if (abs(l[2] - abs(w - l[1])) + l[0] == q) and f == 0:
            f = 1
            print "YES"
        if (abs(q - l[1]) + abs(w - l[2]) == l[0]) and f == 0:
            f = 1
            print "YES"
        if f == 0:
            print "NO"
