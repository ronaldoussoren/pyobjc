"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

REMOTE_REQUIREMENTS = ['netrepr', 'remote_console', 'remote_pipe']

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    app=["PyInterpreter.py"],
    data_files=["PyInterpreter.nib"] + [s+'.py' for s in REMOTE_REQUIREMENTS],
    options=dict(py2app=dict(plist=plist)),
)
