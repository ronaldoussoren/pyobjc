"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    NSPrincipalClass='SillyBalls',
)

setup(
    plugin=['SillyBalls.py'],
    data_files=['English.lproj'],
    options=dict(py2app=dict(
        extension='.saver',
        plist=plist,
    )),
)
