"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleIdentifier = "net.sf.pyobjc.TinyURLService",
    LSBackgroundOnly = 1,
    NSServices = [
        dict(
            NSKeyEquivalent=dict(
                default="0",
            ),
            NSMenuItem=dict(
                default="Shorten URL"
            ),
            NSMessage="doTinyURLService",
            NSPortName="TinyURLService",
            NSReturnTypes=[
                "NSStringPboardType",
            ],
            NSSendTypes=[
                "NSStringPboardType",
            ],
        ),
    ],
)


setup(
    app=["TinyURLService.py"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
