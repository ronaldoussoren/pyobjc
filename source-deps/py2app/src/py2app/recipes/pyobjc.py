import os

def check(cmd, mf):
    m = mf.findNode('_objc')
    if m is None or m.filename is None:
        return None

    return dict(
        flatpackages = [os.path.dirname(m.filename)],
    )
