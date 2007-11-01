"""
Script for building the example, alternative to the Xcode project

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    app=["__main__.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(plist='Info.plist')),
)
