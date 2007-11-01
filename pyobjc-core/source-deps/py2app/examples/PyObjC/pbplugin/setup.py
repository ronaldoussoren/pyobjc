"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

# Copy the hello.pbplugin to:
# ~/Library/Application Support/Apple/Developer Tools/Plug-Ins/
#
# It will just print a bunch of debugging garbage when you start up.

setup(
    plugin=["PyTestPlugin.py"],
    options=dict(py2app=dict(
        extension='.pbplugin',
    )),
)
