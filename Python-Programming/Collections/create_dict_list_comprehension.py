some_list = [(1, "hello"), (2, "I"), (3, "am"), (4, "sandy")]

d = dict(((k, v) for k, v in some_list))
print d

d1 = { k:v for k, v in some_list}

print d1

# No need to go for iterating over list.
d2 = dict(some_list)
print d2