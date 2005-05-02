"""
Script for building the example.

Usage:
        python setup.py py2app
"""
from distutils.core import setup
import py2app
import os


plist = dict(
    NSMainNibFile="MainMenu",
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=['binary'],
            CFBundleTypeMIMETypes=['application/octect-stream'],
            CFBundleTypeName='Binary',
            CFBundleTypeRole='Editor',
            LSTypeIsPackage=False,
            NSDocumentClass='MyDocument',
            NSPersistentStoreTypeKey='Binary',
        ),
        dict(
            CFBundleTypeExtensions=['sql'],
            CFBundleTypeMIMETypes=['application/octect-stream'],
            CFBundleTypeName='SQL',
            CFBundleTypeRole='Editor',
            LSTypeIsPackage=False,
            NSDocumentClass='MyDocument',
            NSPersistentStoreTypeKey='SQLite',
        ),
        dict(
            CFBundleTypeExtensions=['xml'],
            CFBundleTypeMIMETypes=['text/xml'],
            CFBundleTypeName='XML',
            CFBundleOSTypes=['????'],
            CFBundleTypeRole='Editor',
            LSTypeIsPackage=False,
            NSDocumentClass='MyDocument',
            NSPersistentStoreTypeKey='XML',
        ),
    ],
)

# XXX: This should be hidden in a helper module
compiler='/Library/Application Support/Apple/Developer Tools/Plug-ins/XDCoreDataModel.xdplugin/Contents/Resources/momc'
os.system("'%s' MyDocument.xcdatamodel MyDocument.mom"%(compiler,))

setup(
    name='PyOutlineEdit',
    app=["main.py"],
    data_files=["English.lproj", 'MyDocument.mom'],
    options=dict(py2app=dict(plist=plist)),
)
