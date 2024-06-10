from command import cmd


def cmd_version():
    res = cmd(['dokku', 'version'])
    return res.replace('dokku version ','').strip()
