"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=[u'ToDos', u'*'],
            CFBundleTypeName=u'ToDos File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'ToDosDocument',
        ),
    ],
)

setup(
    name='ToDos',
    app=["ToDos.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
)
