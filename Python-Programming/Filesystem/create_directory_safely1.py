import os, errno

try:
    os.makedirs("/home/modak/Codebase/Sand/test")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise