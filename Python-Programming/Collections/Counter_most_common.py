from collections import Counter

c = Counter()

with open("/home/modak/Docs/some_text.txt", "r") as fileobj:
    for line in fileobj:
        l = line.rstrip()
        if l:
            print l
            print
        c.update(line.rstrip().split())
print c
print c.most_common(20)