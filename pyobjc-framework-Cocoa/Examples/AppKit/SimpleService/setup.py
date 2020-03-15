"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {
    "CFBundleIdentifier": "net.sf.pyobjc.PyObjCSimpleService",
    "CFBundleName": "PyObjCSimpleService",
    "LSBackgroundOnly": 1,
    "NSServices": [
        {
            "NSKeyEquivalent": {"default": "F"},
            "NSMenuItem": {"default": "Open File"},
            "NSMessage": "doOpenFileService",
            "NSPortName": "PyObjCSimpleService",
            "NSSendTypes": ["NSStringPboardType"],
        },
        {
            "NSMenuItem": {"default": "Capitalize String"},
            "NSMessage": "doCapitalizeService",
            "NSPortName": "PyObjCSimpleService",
            "NSReturnTypes": ["NSStringPboardType"],
            "NSSendTypes": ["NSStringPboardType"],
        },
    ],
}


setup(
    name="Simple Service",
    app=["SimpleService_main.py"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
