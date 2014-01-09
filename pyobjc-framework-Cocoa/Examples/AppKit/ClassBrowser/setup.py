"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(NSMainNibFile="ClassBrowser")
setup(
    name="ClassBrowser",
    app=["ClassBrowser.py"],
    data_files=["ClassBrowser.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
