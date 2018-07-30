T = int(raw_input())

for _ in xrange(0, T):
    A, B, C, x, y = map(int, raw_input().split())

    if (x-A) + (y-B) == C:
        if x-A < 0 or y-B < 0:
            print "NO"
        else:
            print "YES"
    elif (x-B) + (y-A) == C:
        if (x-B) < 0 or (y-A) < 0:
            print "NO"
        else:
            print "YES"
    elif (x-C) + (y-B) == A:
        if x-C < 0 or y-B < 0:
            print "NO"
        else:
            print "YES"
    elif (x-B) + (y-C) == A:
        if x-B < 0 or y-C < 0:
            print "NO"
        else:
            print "YES"
    elif (x-C) + (y-A) == B:
        if x-C < 0 or y-A < 0:
            print "NO"
        else:
            print "YES"
    elif (x-A) + (y-C) == B :
        if x-A < 0 or y-C < 0:
            print "NO"
        else:
            print "YES"
    else:
        print "NO"




