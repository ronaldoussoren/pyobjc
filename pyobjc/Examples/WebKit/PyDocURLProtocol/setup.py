"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
            NSMainNibFile='PyDocBrowser',
            NSAppleScriptEnabled=True,
            CFBundleURLTypes=[
                dict(
                    CFBundleURLName='Python Documention URL',
                    CFBundleURLSchemes=['pydoc'],
                )
            ]
        )
setup(
    app=["PyDocBrowser.py"],
    data_files=["PyDocBrowser.nib"],
    options=dict(py2app=dict(plist=plist)),
)
