"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    name="PyInterpreter",
    app=["PyInterpreter.py"],
    data_files=["PyInterpreter.nib"],
    setup_requires=["py2app"],
    options=dict(py2app=dict(plist=plist)),
)
