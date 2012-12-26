"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(
    NSPrincipalClass='SillyBalls',
)

setup(
    setup_requires=['py2app'],
    plugin=['SillyBalls.py'],
    data_files=['English.lproj'],
    options=dict(py2app=dict(
        extension='.saver',
        plist=plist,
    )),
)
