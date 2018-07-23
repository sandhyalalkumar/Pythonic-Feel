import itertools
T = int(raw_input())
N, K = map(int, raw_input().split())

while T > 0:
    T = T -1
    seq = map(int, raw_input().split())
    subseq = itertools.combinations(seq, K)
    mnum = 1
    for sub in subseq:
        mine = min(sub)
        maxe = max(sub)
        subb = list(sub)
        subb.remove(mine)
        subb.remove(maxe)
        submul =  reduce(lambda x, y: x*y, subb)
        mnum = mnum * submul
    print mnum




