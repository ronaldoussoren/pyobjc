"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleIdentifier = u'net.sf.pyobjc.TinyURLService',
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
            NSPortName=u'TinyURLService',
            NSSendTypes=[
                u'NSStringPboardType',
            ],
        ),
        dict(
            NSKeyEquivalent=dict(
                default=u'V',
            ),
            NSMenuItem=dict(
                default=u'Shorten URL'
            ),
            NSMessage=u'doTinyURLService',
            NSPortName=u'TinyURLService',
            NSReturnTypes=[
                u'NSURLPboardType',
                u'NSStringPboardType',
            ],
            NSSendTypes=[
                u'NSURLPboardType',
                u'NSStringPboardType',
            ],
        ),
    ],
)


setup(
    app=["TinyURLService.py"],
    options=dict(py2app=dict(plist=plist)),
)
