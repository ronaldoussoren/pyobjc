#
# The build script for the application
#
# This is very likely incorrect, as the application is non-existant at the
# moment.
#
# TODO: Strip 'CVS' directories from the output
from bundlebuilder import buildapp
import os
import sys
from plistlib import Plist, Dict

DB_FILE_TYPE="Python Package Database"

def folderContents(name):
    data = [ 
        os.path.join(name, fn) 
            for fn in os.listdir(name) 
    ]
    return data


buildapp(
    name = "Package Manager",
    mainprogram = "packman.py",
    resources = folderContents("Resources") + [ 'pimp2.py' ],
    nibname = "MainMenu",
    plist = Plist(
        CFBundleIconFile='PackageManager.icns',
        CFBundleDocumentTypes=[
            Dict(
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
    ),
)
