def check(cmd, mf):
    m = mf.findNode('py2app')
    if m is None or m.filename is None:
        return None
    return dict(
        packages = ['py2app'],
    )
