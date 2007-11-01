import sys
def check(cmd, mf):
    m = mf.findNode('pydoc')
    if m is None or m.filename is None:
        return None
    refs = [
        'Tkinter', 'tty', 'BaseHTTPServer', 'mimetools', 'select',
        'threading', 'ic', 'getopt',
    ]
    if sys.platform != 'win32':
        refs.append('nturl2path')
    for ref in refs:
        mf.removeReference(m, ref)
    return dict()
