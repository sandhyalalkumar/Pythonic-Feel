T = int(raw_input())

for _ in xrange(0, T):
    s = raw_input()
    sm = 0
    for e in s:
        if e in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            sm = sm + int(e)
    print sm
