"""
Create an applet from a Python script.

You can drag in packages, Info.plist files, icons, etc.

It's expected that only one Python script is dragged in.
"""

import os, sys
from distutils.core import setup
from plistlib import Plist
import py2app
import tempfile
import shutil
import imp
from py2app.util import copy_tree
try:
    set
except NameError:
    from sets import Set as set

def main():
    scripts = []
    data_files = []
    packages = []
    plist = {}
    iconfile = None
    for fn in sys.argv[1:]:
        fn = os.path.abspath(fn)
        if fn.endswith('.py'):
            if scripts:
                data_files.append(fn)
            else:
                scripts.append(dict(script=fn))
        elif os.path.basename(fn) == 'Info.plist':
            plist = Plist.fromFile(fn)
        elif fn.endswith('.icns'):
            iconfile = os.path.abspath(fn)
        elif os.path.isdir(fn):
            sys.path.insert(0, [os.path.dirname(fn)])
            try:
                path = imp.find_module(os.path.basename(fn))[0]
            except ImportError:
                path = ''
            del sys.path[0]
            if os.path.realpath(path) == os.path.realpath(fn):
                packages.append(os.path.basename(fn))
            else:
                data_files.append(fn)
        else:
            data_files.append(fn)

    build(
        scripts,
        data_files,
        packages=packages,
        plist=plist,
        iconfile=iconfile,
        argv_emulation=True,
    )

def build(scripts, data_files, **options):
    old_argv = sys.argv
    sys.argv = [sys.argv[0], 'py2app']
    old_path = sys.path
    path_insert = set()
    for script in scripts:
        path_insert.add(os.path.dirname(script['script']))
    sys.path = list(path_insert) + old_path
    old_dir = os.getcwd()
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)
    try:
        d = setup(
            app=scripts,
            data_files=data_files,
            options={'py2app':options},
        )
        for target in d.app:
            copy_tree(
                target.appdir,
                os.path.join(
                    os.path.dirname(target.script),
                    os.path.basename(target.appdir),
                ),
                preserve_symlinks=True,
            )

    finally:
        os.chdir(old_dir)
        shutil.rmtree(tempdir, ignore_errors=True)
        sys.argv = old_argv
        sys.path = old_path

if __name__ == '__main__':
    main()
