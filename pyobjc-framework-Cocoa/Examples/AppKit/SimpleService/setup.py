"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleIdentifier = "net.sf.pyobjc.PyObjCSimpleService",
    CFBundleName = "PyObjCSimpleService",
    LSBackgroundOnly = 1,
    NSServices = [
        dict(
            NSKeyEquivalent=dict(
                default="F",
            ),
            NSMenuItem=dict(
                default="Open File",
            ),
            NSMessage="doOpenFileService",
            NSPortName="PyObjCSimpleService",
            NSSendTypes=[
                "NSStringPboardType",
            ],
        ),
        dict(
            NSMenuItem=dict(
                default="Capitalize String",
            ),
            NSMessage="doCapitalizeService",
            NSPortName="PyObjCSimpleService",
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
    name="Simple Service",
    app=["SimpleService_main.py"],
    options=dict(
        py2app=dict(
            plist=plist
        )
    ),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
