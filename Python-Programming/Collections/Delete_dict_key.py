d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

# using del, throw key error
print d
del d["d"]
print d

# handle key error
try:
    del d["e"]
except KeyError:
    pass

# using pop(), throw key error
d.pop("b")
print d

# handle key
d.pop("a", None)
d.pop("f", None)

print d