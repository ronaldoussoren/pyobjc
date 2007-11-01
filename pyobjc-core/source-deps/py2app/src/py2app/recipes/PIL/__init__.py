from py2app.util import imp_find_module
import os, sys, glob
from cStringIO import StringIO

try:
    set
except NameError:
    from sets import Set as set

def check(cmd, mf):
    m = mf.findNode('Image') or mf.findNode('PIL.Image')
    if m is None or m.filename is None:
        return None

    plugins = set()
    visited = set()
    for folder in sys.path:
        if not isinstance(folder, basestring):
            continue
        folder = os.path.realpath(folder)
        if (not os.path.isdir(folder)) or (folder in visited):
            continue
        for fn in os.listdir(folder):
            if not fn.endswith('ImagePlugin.py'):
                continue
            mod, ext = os.path.splitext(fn)
            try:
                imp_find_module(mod)
            except ImportError:
                pass
            else:
                plugins.add(mod)
        visited.add(folder)
    s = StringIO('_recipes_pil_prescript(%r)\n' % list(plugins))
    for plugin in plugins:
        mf.implyNodeReference(m, plugin)
    mf.removeReference(m, 'FixTk')
    # Since Imaging-1.1.5, SpiderImagePlugin imports ImageTk conditionally.
    # This is not ever used unless the user is explicitly using Tk elsewhere.
    sip = mf.findNode('SpiderImagePlugin')
    if sip is not None:
        mf.removeReference(sip, 'ImageTk')

    return dict(
        prescripts = ['py2app.recipes.PIL.prescript', s],
        flatpackages = [os.path.dirname(m.filename)],
    )
