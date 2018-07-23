# os.listdir() will get you everything that's in a directory - files and directories.
# If you want just files, you could either filter this down using os.path:

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]

# or you could use os.walk() which will yield two lists for each directory it visits
# splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

from os import walk
f = []
for (dirpath, dirnames, filenames) in walk("./"):
    f.extend(filenames)
    break