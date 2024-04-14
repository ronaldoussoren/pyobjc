"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {"NSMainNibFile": "PyInterpreter"}

setup(
    name="PyInterpreter",
    app=["PyInterpreter.py"],
    data_files=["PyInterpreter.nib"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
