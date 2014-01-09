"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    NSMainNibFile="PyDocBrowser",
    NSAppleScriptEnabled=True,
    CFBundleURLTypes=[
        dict(
            CFBundleURLName="Python Documention URL",
            CFBundleURLSchemes=["pydoc"],
        )
    ]
)

setup(
    app=["PyDocBrowser.py"],
    data_files=["PyDocBrowser.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-WebKit",
    ]
)
