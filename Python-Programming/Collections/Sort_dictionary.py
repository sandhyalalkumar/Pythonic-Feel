# A dictionary can't be sorted because it is orderless. If you want to sort it convert
# it into other ordered representation.

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

print x.items()
print sorted_x