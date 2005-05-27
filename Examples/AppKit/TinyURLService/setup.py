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
                default=u'0',
            ),
            NSMenuItem=dict(
                default=u'Shorten URL'
            ),
            NSMessage=u'doTinyURLService',
            NSPortName=u'TinyURLService',
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
    app=["TinyURLService.py"],
    options=dict(py2app=dict(plist=plist)),
)
