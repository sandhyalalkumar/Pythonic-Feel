from collections import Counter

name = ["Sandhyalal", "Kumar", "Gond", "Sandhyalal", "Hello", "Gond"]

c =  Counter(name)

print c
print c["Gond"]

name_roll = [
    ("hello", 3),
    ("sandy", 4),
    ("hey", 20),
    ("hey", 20)]

d = Counter(name for name, roll in name_roll)

print d

