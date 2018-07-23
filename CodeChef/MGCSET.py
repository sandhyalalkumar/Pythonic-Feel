import itertools

T = int(raw_input())

while T > 0:
    n, m = map(int, raw_input().split())
    seq = map(int, raw_input().split())
    i = 1
    c = 0
    while i < len(seq):
        sub = itertools.combinations(seq, i)
        li = map(sum, sub)
        for s in li:
            if s%m == 0:
                c = c + 1
        i = i + 1
    print c
    T = T - 1


