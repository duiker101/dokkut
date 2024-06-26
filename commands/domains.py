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


def cmd_domains_add(app, domain):
    res = cmd(['dokku', 'domains:add', app, domain])

    success = res.find('--> Added') > 0
    # TODO error handling

    return True


def cmd_domains_remove(app, domain):
    res = cmd(['dokku', 'domains:remove', app, domain])

    success = res.find('--> Removed') > 0
    # TODO error handling

    return True
