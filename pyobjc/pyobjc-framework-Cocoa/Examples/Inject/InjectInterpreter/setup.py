"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    plugin = ["InjectInterpreterPlugin.py"],
    data_files = ["PyInterpreter.nib"],
    options = dict(py2app=dict(plist=plist)),
)
