"""
Script for building the example.

Usage:
    python2 setup.py py2app
"""
from setuptools import setup

plist = {"NSPrincipalClass": "HotKeyApp"}


setup(
    app=["HotKey.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
