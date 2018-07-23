square = lambda x: x*x
print square(10)

# Lambda on list
l = [1, 2, 3, 4, 5, 6]
l1 = map(lambda x: x*x, l)
print l
print l1