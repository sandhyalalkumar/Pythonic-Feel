# Check os.makedirs: (It makes sure the complete path exists.)
# To handle the fact the directory might exist, catch OSError.
# (If exist_ok is False (the default), an OSError is raised if the target directory already exists.)

import os
try:
    os.makedirs("/home/modak/Codebase/Sand/test")
except OSError:
    pass

