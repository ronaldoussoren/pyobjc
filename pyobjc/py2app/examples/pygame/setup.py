"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

NAME = 'aliens'
VERSION = '0.1'

plist = dict(
    CFBundleIconFile=NAME,
    CFBundleName=NAME,
    CFBundleShortVersionString=VERSION,
    CFBundleGetInfoString=' '.join([NAME, VERSION]),
    CFBundleExecutable=NAME,
    CFBundleIdentifier='org.pygame.examples.aliens',
)

setup(
    data_files=['English.lproj', 'data'],
    app=[
        dict(script="aliens_bootstrap.py", plist=plist),
    ],
    setup_requires=["py2app"],
)
