"""
Script for building the example.

Usage:
    python setup.py py2app
"""
# This is very likely incorrect, as the application is non-existant at the
# moment.
from distutils.core import setup
import py2app

import os
import sys
import glob

DB_FILE_TYPE="Python Package Database"

plist = dict(
    CFBundleName='Package Manager',
    CFBundleIconFile='PackageManager.icns',
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeName=DB_FILE_TYPE,
            CFBundleTypeRole='Editor',
            NSDocumentClass='PackageDatabase',
            # CFBundleTypeIconFile='Package Database.icns',
            CFBundleTypeExtensions = ['packman', 'plist' ],
            CFBundleTypeOSTypes=[],
        ),
    ],

    CFBundleGetInfoString='1.0, Copyright 2004 Ronald Oussoren',
    CFBundleIdentifier='net.sf.pyobjc.PackageManager',
    CFBundleShortVersionString='1.0',
    CFBundleVersion='1.0',

    # We need at least Panther, it may work on Jaguar but I've not yet
    # verified if it should work.
    LSMinimumSystemVersion='10.3.0',

    # We're not apple-scriptable
    NSAppleScriptEnabled='No',
)

setup(
    app=["packman.py"],
    data_files=glob.glob("Resources/*"),
    options=dict(py2app=dict(plist=plist)),
)
