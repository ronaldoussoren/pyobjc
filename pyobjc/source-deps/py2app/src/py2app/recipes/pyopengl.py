def check(cmd, mf):
    m = mf.findNode('OpenGL')
    if m is None or m.filename is None:
        return None
    return dict(
        packages = ['OpenGL'],
    )
