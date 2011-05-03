"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(
    NSPrincipalClass='HotKeyApp',
)
    

setup(
    app=["HotKey.py"],
    data_files=["English.lproj"],
    setup_requires=["py2app"],
    options=dict(py2app=dict(plist=plist)),
)
