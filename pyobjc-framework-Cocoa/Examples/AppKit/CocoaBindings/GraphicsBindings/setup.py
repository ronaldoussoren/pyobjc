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
            CFBundleTypeExtensions=[u'GraphicsBindings', u'*'],
            CFBundleTypeName=u'GraphicsBindings File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'GraphicsBindingsDocument',
        ),
    ],
)

setup(
    app=["GraphicsBindings.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
)
