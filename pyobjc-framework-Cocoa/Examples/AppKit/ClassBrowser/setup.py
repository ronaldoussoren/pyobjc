"""
Script for building the example.

Usage:
    python setup.py py2app
""" 
from distutils.core import setup
import py2app

plist = dict(NSMainNibFile="ClassBrowser")
setup(
    name="ClassBrowser",
    app=["ClassBrowser.py"],
    data_files=["ClassBrowser.nib"],
    options=dict(py2app=dict(plist=plist)),
)
