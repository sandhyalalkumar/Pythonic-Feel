num = [10, 5, 7, 10, 12, 67, 2, 13, 20]

max = reduce(lambda x, y: x if x > y else y, num)
min = reduce(lambda x, y: x if x < y else y, num)

print max
print min