def selectMaxActivities(s, f):
    n = len(s)
    if len(s) <> len(f):
        return []
    else:
        i = 0
        print i
        for j in xrange(n):
            if s[j] >= f[i]:
                i = j
                print j

if __name__ == "__main__":

    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]

    selectMaxActivities(s, f)