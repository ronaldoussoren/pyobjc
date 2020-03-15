"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {"CFBundleName": "FieldGraph"}
setup(
    name="FieldGraph",
    app=["Main.py"],
    data_files=["English.lproj", "CrossCursor.tiff", "Map.png"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
