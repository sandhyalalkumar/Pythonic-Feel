d = {
    "x": 1,
    "y": 2,
    "z": 3,
    "p": 4
}

for key in d:
    print key,

for key, value in d.items():
    print key, value
print

for key,value in d.iteritems():
    print key, value
print

for key in d.iterkeys():
    print key,

print

for value in d.itervalues():
    print value,

print

