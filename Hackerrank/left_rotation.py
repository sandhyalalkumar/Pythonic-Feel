#!/bin/python

np = raw_input().split()
n = int(np[0])
d = int(np[1])

a = map(int, raw_input().strip().split())

array = a[d:]+a[:d]

for element in array:
    print element,


