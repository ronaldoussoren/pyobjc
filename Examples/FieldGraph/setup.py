#!/usr/bin/env python
from distutils.core import setup
import py2app

plist = dict(CFBundleName='FieldGraph')
setup(
    app = ["Main.py"],
    data_files = ["English.lproj", 'CrossCursor.tiff', 'Map.png'],
    options = dict(py2app=dict(plist=plist)),
)
