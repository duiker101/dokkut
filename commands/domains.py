from command import cmd, parse_cmd_lines


def cmd_domains_report(app):
    res = cmd(['dokku', 'domains:report', app])
    lines = parse_cmd_lines(res)

    return {
        'vhost_enabled': lines[0] == 'true',
        'vhost_domains': lines[1].split(' '),
        'global_enabled': lines[2] == 'true',
        'global_domains': lines[3].split(' '),
    }
