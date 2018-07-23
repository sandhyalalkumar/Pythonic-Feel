# zip computes all the list at once, izip computes the elements only when requested.
# One important difference is that 'zip' returns an actual list, 'izip' returns an 'izip object'
# which is not a list and does not support list-specific features (such as indexing)

from itertools import izip

l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 3, 4, 5, 6, 7]

z = zip(l1, l2)
iz = izip(l1, l2)

for a, b in z:
    print a, b
print

for a, b in iz:
    print a, b


