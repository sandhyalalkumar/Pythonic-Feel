import subprocess

def run_cmd(args_list):
    """run linux commands"""
    # import subprocess
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # proc = subprocess.Popen(args_list)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err
    # return s_return

    # cmd=['hdfs', 'dfs', '-ls', '/']


# cmd=['hdfs', 'dfs', '-ls', '/']
(ret, out, err) = run_cmd(['ls', '-ls', '/'])
lines = out.split('\n')

print lines
