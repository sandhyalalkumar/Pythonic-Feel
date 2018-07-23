from __future__ import division
for _ in xrange(input()):
    p,s = map(int,raw_input().split())
    x = (p-(p**2-(4*6*s))**(0.5))/12
    print round(x**(3)-(x**(2))*(p/4)+(x*s)/2,2)