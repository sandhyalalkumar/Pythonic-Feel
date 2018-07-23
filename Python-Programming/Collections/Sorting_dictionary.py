x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print x.items()
print sorted(x.values())

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print sorted_x

# sorted_x will be a list of tuples sorted by the second element in each tuple. dict(sorted_x) == x.
# And for those wishing to sort on keys instead of values:

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print sorted_x

