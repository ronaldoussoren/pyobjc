def check(cmd, mf):
    name = 'cjkcodecs'
    m = mf.findNode(name)
    if m is None or m.filename is None:
        return None
    mf.import_hook(name, m, ['*'])
    return dict()
