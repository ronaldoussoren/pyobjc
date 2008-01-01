"""
Script for building the example, alternative to the Xcode project.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    name="TableModel",
    app=["__main__.py"],
    data_files=["English.lproj"],
)
