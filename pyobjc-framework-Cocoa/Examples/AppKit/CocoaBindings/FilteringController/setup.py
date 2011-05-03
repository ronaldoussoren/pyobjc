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
            CFBundleTypeExtensions=[u'FilteringController', u'*'],
            CFBundleTypeName=u'FilteringController File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'FilteringControllerDocument',
        ),
    ],
)

setup(
    name='FilteringController',
    app=["FilteringController.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
)
