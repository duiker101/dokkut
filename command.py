import subprocess


def cmd(args):
    sudo_password = 'once'
    cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(['sudo','-S'] + args, stdin=cmd1.stdout, stdout=subprocess.PIPE)
    output = cmd2.stdout.read().decode()
    return output

    # cmd2 = subprocess.run(args)
    # return cmd2

    # cmd2 = subprocess.Popen(args, stdout=subprocess.PIPE)
    # output = cmd2.stdout.read().decode()
    # return output

def parse_cmd_lines(output):
    return [l.split(':')[1].strip() for l in output.strip().split('\n')[1:]]