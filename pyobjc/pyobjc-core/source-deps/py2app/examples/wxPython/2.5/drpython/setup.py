from distutils.core import setup
import py2app
import os
VERSION = '3.10.1'
PATH = 'drpython-%s' % (VERSION,)
script = []
includes = []
data_files = []
for name in os.listdir(PATH):
    if name.startswith('.') or name == 'CVS':
        continue
    fn = os.path.join(PATH, name)
    mod, ext = os.path.splitext(name)
    if ext == '.pyw':
        script.append(fn)
    elif ext == '.py':
        includes.append(mod)
    elif ext == '.pyc':
        continue
    else:
        data_files.append(fn)

setup(
    app = script,
    data_files = data_files,
    options = dict(py2app=dict(
        includes = includes,
        argv_emulation = True,
    )),
)
