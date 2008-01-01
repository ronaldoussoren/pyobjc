"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    NSPrincipalClass='HotKeyApp',
)
    

setup(
    app=["HotKey.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(plist=plist)),
)
