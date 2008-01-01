import os
def check(cmd, mf):
    m = mf.findNode('OpenGL')
    if m is None or m.filename is None:
        return None
    p = os.path.splitext(m.filename)[0] + '.py'
    # check to see if it's a patched version that doesn't suck
    if os.path.exists(p):
        for line in file(p, 'rU'):
            if line.startswith('__version__ = '):
                return dict()
    # otherwise include the whole damned thing
    return dict(
        packages = ['OpenGL'],
    )
