"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

import glob
images = glob.glob('Images/*.tiff')
icons = glob.glob('Icons/*.icns')

plist = dict(
    CFBundleShortVersionString='To Do v1',
    CFBundleIconFile='ToDoApp.icns',
    CFBundleGetInfoString='To Do v1',
    CFBundleIdentifier='net.sf.pyobjc.ToDo',
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeName='To Do list',
            CFBundleTypeRole='Editor',
            NSDocumentClass='ToDoDocument',
            CFBundleTypeIconFile='ToDoDoc.icns',
            CFBundleTypeExtensions=['ToDo'],
            CFBundleTypeOSTypes=['ToDo'],
        ),
    ],
    CFBundleName='To Do',
)

setup(
    app=["main.py"],
    data_files=["English.lproj" ] + images + icons,
    options=dict(py2app=dict(plist=plist)),
)
