"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
from itertools import imap, chain
import glob
import py2app
import os, sys
try:
    set
except NameError:
    from sets import Set as set

NAME = 'wxGlade'
VERSION = '0.3.4'
WXDIR = '%s-%s' % (NAME, VERSION)

# these are files and packages
WIDGETS = os.path.join(WXDIR, 'widgets', '')
# these are files
CODEGEN = os.path.join(WXDIR, 'codegen', '')

def data_files_as_code(mf, wxdir):
    for fn in os.listdir(wxdir):
        if os.path.exists(os.path.join(wxdir, fn, '__init__.py')):
            mf.import_hook(fn, None, ['*'])
        elif fn.endswith('.py'):
            mf.import_hook(fn[:-len('.py')])

# make sure it can find everything it wants
sys.path[:0] = [WXDIR, WIDGETS, CODEGEN]

class wxglade_recipe(object):
    def check(self, dist, mf):
        m = mf.findNode('wxglade')
        if m is None:
            return None
        paths = [os.path.join(os.path.realpath(p), '') for p in (WIDGETS, CODEGEN)]
        for path in paths:
            data_files_as_code(mf, path)
        def filterfunc(mod, paths=paths):
            for path in paths:
                if getattr(mod, 'filename', '').startswith(path):
                    return False
            return True
        return dict(
            filters=[filterfunc],
        )

def get_data_files(paths):
    lst = []
    for f in paths:
        lst.extend(glob.glob(os.path.join(WXDIR, f)))
    return [('', lst)]

import py2app.recipes
py2app.recipes.wxglade = wxglade_recipe()

setup(
    app=['wxGlade.py'],
    data_files=get_data_files([
        '*.txt', 'docs', 'res',
        'widgets', 'codegen', 'icons'
    ]),
    options=dict(py2app=dict(
        argv_emulation=True,
        compressed=True,
    )),
)
