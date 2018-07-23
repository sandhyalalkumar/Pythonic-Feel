import subprocess

def run_cmd(cmd):
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
    stddata = proc.communicate()
    returncode = proc.returncode
    return returncode
    # return stddata, returncode

cmd = ["dfs", "-l"]
returncode = run_cmd(cmd)
print returncode

"""
cmd = ["tree"]
data, returncode = run_cmd(cmd)
print data, returncode
"""
