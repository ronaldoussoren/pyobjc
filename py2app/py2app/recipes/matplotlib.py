def check(cmd, mf):
    m = mf.findNode('matplotlib')
    if m is None or m.filename is None:
        return None
    mf.import_hook('pytz.zoneinfo', m, ['UTC'])
    return dict(
        packages = ['matplotlib']
    )
