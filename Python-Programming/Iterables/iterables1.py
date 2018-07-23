def list_iterables():

    random_list = [1, 2, 4, "Hello", 2.45, ["T"], ("Sandhyalal", 1234)]

    for i in random_list:
        print i

def dict_iterables():

    random_dict = {
        1: "456",
        "name": 123,
        2: [1, 2, 3]
    }

    for k in random_dict:
        print k

    for k in random_dict.iterkeys():
        print k

    # Returns a generators, lazy, not memory intensive.
    for k, v in random_dict.iteritems():
        print k, v

    # Returns a list of tuples, memory intensive, all the elements are copied.
    for k, v in random_dict.items():
        print k, v

def pattern_iterables():
    import re
    text = "hellothisisnotlowercasehelloworld"
    pattern = "hello"

    for match in re.finditer(pattern, text):
        print match

def itertools_iterables():
    # Once for each integer...infinte !
    import itertools
    for a in itertools.count():
        print a

def dir_iterables():

    import os
    for root, dirs, files in os.walk('/home/modak/Codebase/Projetcs/Python-algorithms'):
        print root
        print dirs
        print files

if __name__ == "__main__":

    list_iterables()
    dict_iterables()
    pattern_iterables()
    # itertools_iterables()
    dir_iterables()
