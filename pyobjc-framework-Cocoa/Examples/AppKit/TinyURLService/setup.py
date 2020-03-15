"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {
    "CFBundleIdentifier": "net.sf.pyobjc.TinyURLService",
    "LSBackgroundOnly": 1,
    "NSServices": [
        {
            "NSKeyEquivalent": {"default": "0"},
            "NSMenuItem": {"default": "Shorten URL"},
            "NSMessage": "doTinyURLService",
            "NSPortName": "TinyURLService",
            "NSReturnTypes": ["NSStringPboardType"],
            "NSSendTypes": ["NSStringPboardType"],
        }
    ],
}


setup(
    app=["TinyURLService.py"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
