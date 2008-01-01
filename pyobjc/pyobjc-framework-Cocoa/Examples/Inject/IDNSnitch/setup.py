"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup, Extension
import py2app

# Plugin
plugin = setup(
    plugin = ["IDNSnitchPlugin.py"],
)
plugin_dir = plugin.plugin[0].appdir

app = setup(
    app = ["IDNSnitch.py"],
    data_files = [plugin_dir, "English.lproj"],
)
app_dir = app.app[0].appdir

import os
if os.path.exists(app_dir):
    app_dir = os.path.join(app_dir, '')
    plugin_dir = os.path.join(app_dir, 'Contents', 'Resources', os.path.basename(plugin_dir), '')
    for root, dirs, files in os.walk(plugin_dir):
        for fn in files:
            if not os.path.splitext(fn)[1] == '.so':
                continue
            base = root[len(app_dir):]
            rbase = root[len(plugin_dir):]
            dots = '/'.join(['..'] * len(base.split(os.sep)))
            rsrc = os.path.join(app_dir, rbase, fn)
            dst = os.path.join(root, fn)
            if os.path.exists(rsrc):
                os.unlink(dst)
                os.symlink(os.path.join(dots, rbase, fn), dst)
