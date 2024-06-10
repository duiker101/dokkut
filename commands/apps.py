from command import cmd, parse_cmd_lines


def cmd_apps_list():
    res = cmd(['dokku', 'apps:list'])
    return res.strip().split('\n')[1:]


def cmd_app_report(app):
    res = cmd(['dokku', 'apps:report', app])
    lines = parse_cmd_lines(res)

    return {
        'created': lines[0],  # created
        'source': lines[1],  # source
        'source_meta': lines[2],  #
        'dir': lines[3],
        'locked': lines[4],
    }
