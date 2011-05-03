"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleIdentifier = u'net.sf.pyobjc.PyObjCSimpleService',
    CFBundleName = u'PyObjCSimpleService',
    LSBackgroundOnly = 1,
    NSServices = [
        dict(
            NSKeyEquivalent=dict(
                default=u'F',
            ),
            NSMenuItem=dict(
                default=u'Open File',
            ),
            NSMessage=u'doOpenFileService',
            NSPortName=u'PyObjCSimpleService',
            NSSendTypes=[
                u'NSStringPboardType',
            ],
        ),
        dict(
            NSMenuItem=dict(
                default=u'Capitalize String',
            ),
            NSMessage=u'doCapitalizeService',
            NSPortName=u'PyObjCSimpleService',
            NSReturnTypes=[
                u'NSStringPboardType',
            ],
            NSSendTypes=[
                u'NSStringPboardType',
            ],
        ),
    ],
)


setup(
    name='Simple Service',
    app=["SimpleService_main.py"],
    options=dict(py2app=dict(plist=plist)),
)
