l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = filter(lambda x: x > 5, l)

print l
print l1

fun = lambda x: 'big' if x > 5 else 'small'
print fun(10)
print fun(5)



