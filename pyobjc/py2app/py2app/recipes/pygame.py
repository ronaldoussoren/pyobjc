import os
def check(cmd, mf):
    m = mf.findNode('pygame')
    if m is None or m.filename is None:
        return None
    def addpath(f):
        return os.path.join(os.path.dirname(m.filename), f)
    RESOURCES = ['freesansbold.ttf', 'pygame_icon.tiff', 'pygame_icon.icns']
    return dict(
        loader_files = [
            ('pygame', map(addpath, RESOURCES)),
        ],
    )
