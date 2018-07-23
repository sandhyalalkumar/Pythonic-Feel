T = int(raw_input())

for _ in xrange(0, T):
    s, e = map(int, raw_input().split())
    c = 0
    for num in xrange(s, e+1):
        number = str(num)
        if number[-1] in ["2", "3", "9"]:
            c = c + 1
    print c

